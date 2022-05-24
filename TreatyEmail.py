import time, os
import requests

def sendEmail(email, information,flag):
    'sends message to the owner (picture of the pet)'
    
    EVENT = "pet_detected"
    BASE_URL = 'https://maker.ifttt.com/trigger/'
    KEY = 'cNFKN8ywlG5SOJEu0TMCHR'

    url = BASE_URL + EVENT  + '/with/key/' + KEY
    response = requests.post(url, json=data)
    print(response.status_code)
    print("No more notifications for:" + str(TimeB4Txt) +" mins")
    time.sleep(TimeB4Txt * 60)
