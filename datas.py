import json
import urllib.request, urllib.parse, urllib.error
import ssl
from urllib.parse import quote


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def bookid(title):
    url1 = 'https://frappe.io/api/method/frappe-library?title='+quote(title)
    url2 = 'https://frappe.io/api/method/frappe-library?authors='+quote(title)
    url3 = 'https://frappe.io/api/method/frappe-library?publisher='+quote(title)
    #print(url)
    book1=urllib.request.urlopen(url1)
    data1=book1.read().decode()
    author1=urllib.request.urlopen(url2)
    data2=author1.read().decode()
    publisher1=urllib.request.urlopen(url3)
    data3=publisher1.read().decode()
    #print(data)
    bookidx=[]
    titlex=[]
    pagesx=[]
    authorx=[]
    publisherx=[]
    info1 = json.loads(data1)
    info2 = json.loads(data2)
    info3 = json.loads(data3)
    info = info1['message'] + info2['message'] + info3['message']

    #bookid = input('Enter Reference ID: ')
    #print(info['message'][0]['bookID'])
    for item in info:
        if item['bookID'] not in bookidx:
            bookidx.append(item['bookID'])
            titlex.append(item['title'])
            pagesx.append(item['  num_pages'])
            authorx.append(item['authors'])
            publisherx.append(item['publisher'])
    return titlex ,authorx, publisherx
