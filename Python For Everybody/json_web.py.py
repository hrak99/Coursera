import urllib.request, urllib.parse, urllib.error
import json


user_url = input('Enter location: ')
if len (user_url)<1: user_url = "http://py4e-data.dr-chuck.net/comments_130475.json"
url = user_url + urllib.parse.urlencode({})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print(data)
print('Retrieved', len(data), 'characters')

info = json.loads (data)
#print (json.dumps (info, indent=4))
print("count", len (info))
sum = 0
print(info["comments"])
for item in info['comments']:
    count = (item["count"])
    #print (count)
    int(count)
    sum = sum + count
print (sum)



#    print (s)

#print (s)
