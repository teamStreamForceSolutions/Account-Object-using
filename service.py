import cgi
import requests
from simple_salesforce import Salesforce

sf = Salesforce(username='kalyanprchowdary@gmail.com', password='Kalyan@117', security_token='8779811613588378217')
sf.Case.update('0017F000002JM5BQAW', {'Description': 'New Description updated'})

# login here:
# https://login.salesforce.com/services/oauth2/authorize?response_type=code&client_id=3MVG9A2kN3Bn17hsWsLDatw._IVMEUBoPKv.7ksp0tz7xLX4tWDVgyzwTCA7i_yTfP.qYuNOsSoPNcdVH6DuE&redirect_uri=http://localhost/cgi-bin/python/oauth.py

consumer_key = '3MVG9A2kN3Bn17hsWsLDatw._IVMEUBoPKv.7ksp0tz7xLX4tWDVgyzwTCA7i_yTfP.qYuNOsSoPNcdVH6DuE'
consumer_secret = '8779811613588378217'
request_token_url = 'https://login.salesforce.com/services/oauth2/token'
access_token_url = 'https://login.salesforce.com/services/oauth2/token'
redirect_uri = 'http://localhost/cgi-bin/python/oauth.py'
authorize_url = 'https://login.salesforce.com/services/oauth2/authorize'  # ?response_type=token&client_id='+consumer_key+'&redirect_uri='+redirect_uri

query = cgi.FieldStorage()
req = None

if 'login' in query:
    print()
"Location: https://login.salesforce.com/services/oauth2/authorize?response_type=code&client_id=" + consumer_key + "&redirect_uri=" + redirect_uri
print()
if 'code' in query:
    code = query.getvalue('code')

data = dict(grant_type='authorization_code', redirect_uri=redirect_uri, code=code, client_id=consumer_key,
            client_secret=consumer_secret)
headers = {
    'content-type': 'application/x-www-form-urlencoded'
}
req = requests.post(access_token_url, data=data, headers=headers)
response = req.json()
sf = Salesforce(instance_url=response['instance_url'], session_id=response['access_token'])
records = sf.query("SELECT Id, Name, Email FROM Contact")
records = records['records']

# print web page
print()
"Content-type: text/html"
print()

print()
"<html><body>"
print()
"<h1>SELECT Id, Name, Email FROM Contact</h1>"
print()
"<table>"
print()
"<tr><td><b>Name</b></td><td><b>Email</b></td></tr>"
for record in records:
    print()
"<tr><td>" + records['Name'] + "</td><td>" + records['Email'] + "</td></tr>"
print()
"</table>"
print()
"</body></html>"
