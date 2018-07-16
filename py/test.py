import requests
from glob import glob
res = requests.get('http://0.0.0.0:9200')
print(res.content)
inputfiles=glob("/Users/timothyhseed/Library/Mobile\ Documents/com~apple~CloudDocs/")
for f in inputfiles:
  print("Need to Add {}".format(i))
