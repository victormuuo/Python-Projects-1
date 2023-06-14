import requests
import schedule
import time



def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '+254797447062',
        'message': 'Hello Victor😝....How are you?😜',
        'key': 'textbelt',
    })
    print(resp.json())

schedule.every(10).seconds.do(send_message) 
while True:
    schedule.run_pending()
    time.sleep(1)   