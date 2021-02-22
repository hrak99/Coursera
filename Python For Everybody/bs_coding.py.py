import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url= input ("Enter Url") # " http://py4e-data.dr-chuck.net/known_by_Fikret.html"
user_count = input ("Enter Count")
count = int (user_count)
user_position = input ("Enter Position")
position = int (user_position)
while count > 0:
    html= urllib.request.urlopen(url,context=ctx).read()
    soap = BeautifulSoup (html,'html.parser')
#print (soap)
    tags  = soap ('a')
    tags_list = list()
    for tag in tags:
        links = (tag.get('href',None))
        tags_list.append(links)
    url = tags_list [position]
    print ("Retrieving", url)
    count = count - 1
    
