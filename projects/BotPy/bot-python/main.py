'''
Created on 20/05/2016

@author: Carlos
'''

import mechanize
from firebase.firebase import FirebaseApplication
from BeautifulSoup import BeautifulSoup
from _socket import timeout

timeout = 5000
data = ""

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]

response = br.open("http://portal.suframa.gov.br/PMNRecEViewController/")
# response = br.open('http://www.google.com/')

print response.code

''' Acessando login
'''
print 'Efetuando login' 

br.select_form("AutenticarUsuarioForm")
br.form["cnpj"] = "45.242.914/0286-11"
br.form["senha"] = "2016LOJAMAP"

respSubmit = br.submit()

print respSubmit.code
print 'Login efetuado'
# print respSubmit.get_data()

''' acessando link de consulta de nota fiscal
'''
print 'Acessando tela de consulta'
respNota = br.open("/PMNRecEViewController/prepararDadosNotaFiscal.do?metodo=preparar")

print respNota.code
#print respNota.get_data()

''' acessando form de consta de nota fiscal
'''
print 'Consultando nota fiscal'
br.select_form("ConsultaSituacaoNotaFiscalForm")
#br.form["numeroNotaFiscal"] = ""
br.form["tipoNotaFiscal"] = ["2"]
br.form["chaveAcesso"] = "35150145242914004518550010004261151690070495"
respConsulta = br.submit()

''' retorno da consulta
'''
print respConsulta.code
#print respConsulta.get_data()

soup = BeautifulSoup(respConsulta.get_data())
table = soup.find(id="tbNotasFiscaisEletronicas")
# print table


print "processando retorno"

headers = [item.text for item in table('th')]

for row in table.findAll('tr')[1:]:
    col = row.findAll('td')
    lote = col[1].string
    print 'Lote: ', lote
    chaveAcesso = col[2].string
    print 'Chave de Acesso', chaveAcesso
    dataProcessamento = col[3].string
    print 'Data de Processamento', dataProcessamento
    situacao = col[4].string
    print 'Situacao', situacao
    record = (lote, chaveAcesso, dataProcessamento, situacao)
    #print "|".join(record)

#for row in table('tr')[1:]:
#    params = [item.text.strip() for item in row('td')]
#    print dict(zip(headers, params))

fb =  FirebaseApplication('https://py-firebase.firebaseio.com/', None)
new_user = 'Ozgur Vatansever'

responsePost = fb.post('/users', new_user, connection=None, params={'print': 'silent'}, headers={'X_FANCY_HEADER': 'VERY FANCY'})
print responsePost