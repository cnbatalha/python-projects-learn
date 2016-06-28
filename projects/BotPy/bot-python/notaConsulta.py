'''
Created on 24/05/2016

@author: Carlos
'''

import re
import firebaseConnect
import mechanize
import time
from BeautifulSoup import BeautifulSoup
from _socket import timeout

def getLogin():
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
    
    respSubmit = br.submit()
    
    print respSubmit.code
    print 'Login efetuado'
    # print respSubmit.get_data()
    
    return br
    
def consultaPIN(periodo):
    br = getLogin()

    ''' acessando link de consulta PIN
    '''
    print 'Acessando tela de consulta - PIN'
    respNota = br.open("/PMNRecEViewController/prepararConsultaSituacaoPinAction.do?metodo=preparar")
    
    print respNota.code
    #print respNota.get_data()
    
    br.select_form("ConsultaResultPINForm")
    #br.form["numeroNotaFiscal"] = ""
    br.form["dataInicial"] = '20/05/2016'
    br.form["dataFinal"] = '28/05/2016'
    respConsulta = br.submit()

    # print respConsulta.get_data()
    
    soup = BeautifulSoup(respConsulta.get_data())
    table = soup.find(id="tbPinsResult")   
    
    # carregando lista de PINs
    PINs = list()     
    for row in table.findAll('tr')[1:]:
        col = row.findAll('td')
        pin = col[0]
        print pin.text
        PINs.append(pin.text)
     
    # consultando pin individual   
    for pin in PINs:      
        consultaNotasPIN(br, pin)
            
    return ''

def consultaNotasPIN( br, pin):
    print 'Acessando tela de consulta - PIN'
    respNota = br.open("/PMNRecEViewController/prepararConsultaSituacaoPinAction.do?metodo=preparar")    
    print respNota.code
    #print respNota.get_data()
    
    br.select_form("ConsultaResultPINForm")
    #br.form["numeroNotaFiscal"] = ""
    br.form["dataInicial"] = '20/05/2016'
    br.form["dataFinal"] = '28/05/2016'
    respConsulta = br.submit()

    respNota = br.open("/PMNRecEViewController/prepararConsultaSituacaoPinAction.do?metodo=visualizarDados&idPIN=" + pin)
    
    print respNota.code
    print respNota.get_data()

    soup = BeautifulSoup(respNota.get_data())
    table = soup.find(id="tbNotasFiscaisEletronicas")
    # print table
            
    print "processando retorno"    
    headers = [item.text for item in table('th')]
    saveNotas(table, 0)
    br.back()
    time.sleep(3)
        
def consulta( chave):
    br = getLogin()
    
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
    saveNotas(table, 1)
    
        
def saveNotas(table, colIndex):
    
    dados = dict()
    
    for row in table.findAll('tr')[1:]:
        col = row.findAll('td')
        lote = col[colIndex].string
        dados['lote'] = lote
        print 'Lote: ', lote
        colIndex = colIndex + 1
        chaveAcesso = col[colIndex].string
        dados['chave'] = chaveAcesso
        print 'Chave de Acesso', chaveAcesso
        colIndex = colIndex + 1
        dataProcessamento = col[colIndex].string
        dados['dataProcessamento'] = dataProcessamento
        print 'Data de Processamento', dataProcessamento
        colIndex = colIndex + 1
        situacao = col[colIndex].string
        dados['situacao'] = situacao
        print 'Situacao', situacao
        dados['dataCadastro'] = time.strftime('%d/%m/%Y')
        
        firebaseConnect.post('notas/', dados)

    