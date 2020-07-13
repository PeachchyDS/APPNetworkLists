import requests
from akamai.edgegrid import EdgeGridAuth,EdgeRc
from urlparse import urljoin
#Credential authentication
edgerc = EdgeRc('/home/witadmin/.edgerc')
section = 'default'
a = edgerc.get(section,'host')
baseurl = 'https://%s' % edgerc.get(section, 'host')
s = requests.Session()
s.auth=EdgeGridAuth.from_edgerc(edgerc, section)
path='/network-list/v2/network-lists?'
#networklist name.
search = input('Networklist name:')
#true or false.
iE = input('includeElement:')
#true or false.
extend = input('Extended:')
#IP or GEO.
listType = input('ListType:')
w = '&search='+search
x = 'includeElements='+iE
y = '&extended='+extend
z = '&listType='+listType
#Get information from Akamai server.
full_path=path+x+w+y+z
url = urljoin(baseurl,full_path)
a = s.get(url)
print(a)
