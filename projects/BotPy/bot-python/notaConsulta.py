'''
Created on 24/05/2016

@author: Carlos
'''

import firebaseConnect
import mechanize
from BeautifulSoup import BeautifulSoup
from _socket import timeout

def consulta( chave):
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
    br.form["cnpj"] = ""
    br.form["senha"] = ""
    
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
    br.form["chaveAcesso"] = chave
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
    
    dados = dict()
    
    for row in table.findAll('tr')[1:]:
        col = row.findAll('td')
        lote = col[1].string
        dados['lote'] = lote
        print 'Lote: ', lote
        chaveAcesso = col[2].string
        dados['chave'] = chaveAcesso
        print 'Chave de Acesso', chaveAcesso
        dataProcessamento = col[3].string
        dados['dataProcessamento'] = dataProcessamento
        print 'Data de Processamento', dataProcessamento
        situacao = col[4].string
        dados['situacao'] = situacao
        print 'Situacao', situacao
        
        firebaseConnect.post('notas/', dados)
        # record = (lote, chaveAcesso, dataProcessamento, situacao)
        # print "|".join(record)
    
    #for row in table('tr')[1:]:
    #    params = [item.text.strip() for item in row('td')]
    #    print dict(zip(headers, params))

