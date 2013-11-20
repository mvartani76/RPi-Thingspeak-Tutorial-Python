#Pushing data to Thingspeak
# python
import httplib, urllib
params = urllib.urlencode({'field1': 12, 'field2': 11,'key':'VUG7LG3DBYL3YOLK'})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept":  
    "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print response.status, response.reason

data = response.read()
conn.close()
