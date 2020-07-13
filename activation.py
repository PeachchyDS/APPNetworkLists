import requests
from akamai.edgegrid import EdgeGridAuth
from urllib.parse import urljoin
baseurl = 'https://akab-cqptmeb6tggffsed-d424vrqh6bzudp5x.luna.akamaiapis.net'
s = requests.Session()
s.auth =EdgeGridAuth(
    client_secret = 'mTrOuyijM4v9AOTyS/Bj3p7Y4eZYZXaNWhPyZONjBLs=',
    access_token = 'akab-gvmzkdn5cjulstcy-2lgvtt22p7gpxm4j',
    client_token = 'akab-qwmgpij6vabq54mc-zwwerwa2fb3vrlmb'
    )
#Activate list.
path='/network-list/v2/network-lists/'
x = input('Network ID:')
y = input('Environment:')
full_path= path+x+'/environments'+'/'+y+'/activate'
url = urljoin(baseurl,full_path)
comments = input()
emails = input()
data = {'comments':comments,
        'notificationRecipients':[emails]
        }
c = s.post(url,json=data)
print(c.json())
print(c.status_code)
print(c.headers)
