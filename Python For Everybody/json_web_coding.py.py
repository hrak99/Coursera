import urllib.request,urllib.parse,urllib.error
import json
urlservice = "http://py4e-data.dr-chuck.net/geojson?"
location = input ("Enter the location")
url = urlservice + urllib.parse.urlencode({"address":location})
print ("Retrrieving:", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print ('Retrieved',len(data),'characters')

info = json.loads(data)

print (json.dumps(info,indent = 4))
print (info["results"])
for item in info ["results"]:
    place_id = (item["place_id"])
print ("place_id", place_id)
