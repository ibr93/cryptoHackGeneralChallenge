#!/usr/bin/python
import requests, json, sys
target = 'cryptohack.org'
req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

json_data = json.loads(req.text)
for (key,value) in enumerate(json_data):
    url = str(value['name_value'])
    if url.endswith(target):
        try:
            response_req = requests.get('https://' +url).text
        
            if(response_req.startswith('crypto')):
                print('URL : ' + url)
                print('KEY : ' +response_req)
                break         
        except:
            continue