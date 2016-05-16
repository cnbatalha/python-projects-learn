import urllib
import json
import urllib2

jReq = urllib2.Request('http://sistemajubilus.com.br:8080/sisigreja-server/oauth/token?grant_type=password&username=SISIGREJASITE&password=SISIGREJASITE')

req = urllib2.Request('https://us3.api.mailchimp.com/3.0/lists')
req.add_header('Authorization', 'Basic Y25iYXRhbGhhLnNpc3RlbWF0aWM6ZWFmYjdlYzRiYTE3ZWMzZWQwNjg2Y2MwOWNjZTYxN2UtdXMz')
resp = urllib2.urlopen(req)
content = resp.read()

# print content
info = json.loads(content)

for item in info['lists']:
    print '------------------------------------------------------'
    print item['name']
    membersUrl = 'https://us3.api.mailchimp.com/3.0/lists/' + item['id'] + '/members'
    print membersUrl
    membrosReq = req = urllib2.Request(membersUrl)
    membrosReq.add_header('Authorization', 'Basic Y25iYXRhbGhhLnNpc3RlbWF0aWM6ZWFmYjdlYzRiYTE3ZWMzZWQwNjg2Y2MwOWNjZTYxN2UtdXMz') 
    mResp = urllib2.urlopen(req) 
    mContent = json.loads(mResp.read()) 
    for m in mContent['members']:
        print m['email_address']



