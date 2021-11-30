import requests
from pprint import pprint
name = input('input username')
req = requests.get('https://api.github.com/users/'+name+'/repos')
json = req.json()
if req.ok:
    print("CONNECT!")
    for i in range(0, len(json)):
        print("№ repo:", i + 1)
        print("Name repo:", json[i]['name'])
        print("URL repo:", json[i]['url'], '\n')
    'pprint(json)'
    pass
else:
    print("Not CONNECTED!/user not found")
    pass
