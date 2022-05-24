import time, os
import requests

def sendMSG(number, information,flag):
    'sends message to the owner (picture of the pet)'
    

    BASE_URL = 'https://api.thingspeak.com/apps/...'
    KEY = 'INSERT KEY'
    
    status = 'ThingMsg: Motion has been detected.'
    data = {'api_key' : KEY, 'status' : status}
    response = requests.post(BASE_URL, json=data)
    print(response.status_code)
