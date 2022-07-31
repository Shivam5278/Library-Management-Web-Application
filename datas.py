import json
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib.parse import quote


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
title = input('Enter Name: ')

url = 'https://frappe.io/api/method/frappe-library?title='+quote(title)
print(url)
fhand=urllib.request.urlopen(url)
data=fhand.read().decode()
#print(data)
bookidx=[]
titlex=[]
pages=[]
info = json.loads(data)
#bookid = input('Enter Reference ID: ')
#print(info['message'][0]['bookID'])
for item in info['message']:
    bookidx.append(item['bookID'])
    titlex.append(item['title'])
    pages.append(item['  num_pages'])

#bookid = input('Enter Reference ID: ')
#a=bookidx.index(bookid)
for i in titlex:
    print(i)
print(bookidx[1],':     ', titlex[1],'  Pages:',pages[1])
#{"error":"Invalid Parameters","total_records":4000,"allowed_params":["title","authors","isbn","publisher","page"]}
