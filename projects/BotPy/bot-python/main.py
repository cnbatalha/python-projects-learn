'''
Created on 20/05/2016

@author: Carlos
'''

import mechanize
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
br.select_form("AutenticarUsuarioForm")
br.form["cnpj"] = ""
br.form["senha"] = ""

respSubmit = br.submit()

print respSubmit.code
# print respSubmit.get_data()

''' acessando link de consulta de nota fiscal
'''
respNota = br.open("/PMNRecEViewController/prepararDadosNotaFiscal.do?metodo=preparar")

print respNota.code
# print respNota.get_data()

''' acessando form de consta de nota fiscal
'''
br.select_form("ConsultaSituacaoNotaFiscalForm")
br.form["numeroNotaFiscal"] = ""
respConsulta = br.submit()

''' retorno da consulta
'''
print respConsulta.code
print respConsulta.get_data()

