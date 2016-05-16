'''
Created on 13/05/2016

@author: Carlos
'''
import urllib
import json

url = "C:\Users\Carlos\git\python-projects-learn\coursera\PythonCoursera\chapter13-json\comments_194821.json"
content = open(url).read()

# print content
info = json.loads(content)
soma = 0

for comment in info["comments"]:
    #print comment
    soma = soma + comment["count"]

print soma