import requests
import json
from akamai.edgegrid import EdgeGridAuth,EdgeRc
from urlparse import urljoin
edgerc = EdgeRc('/home/witadmin/.edgerc')
section = 'default'
a = edgerc.get(section,'host')
baseurl = 'https://%s' % edgerc.get(section, 'host')
s = requests.Session()
s.auth=EdgeGridAuth.from_edgerc(edgerc, section)
FileName = input('File Name:')
netlist_id= input('Network List ID:')
with open(FileName, 'r') as f:
    address = [line.strip() for line in f]
path = '/network-list/v2/network-lists/'
full_path = path+netlist_id+'/append'
url = urljoin(baseurl,full_path)
data ={"list": address}
ap = s.post(url,json=data)
result=ap.json()
print(json.dumps(result))
