import requests
import json
from django.http import HttpResponse


API_KEY = 'MWIwOTYxMjItMWI5MC00Njg2LWE5N2UtN2ZkMGM3NmE2ZTc1OmE4ZmQ1Nzc4LTMwM2EtNDMyNC04Zjg5LWNlYWViMWVhNDMzZQ=='

requests.packages.urllib3.disable_warnings() # отключает надоедливые warnings SSL (из-за минцифр)

def connect_gigachat():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    payload={
    'scope': 'GIGACHAT_API_PERS'
    }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': 'cb3585af-8426-4a4c-8f9f-fa0495dd740d',
    'Authorization': f'Basic {API_KEY}'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        global ACCESS_TOKEN
        ACCESS_TOKEN = response.json()['access_token']
    except Exception as ex:
      return HttpResponse(f'Произошла ошибка: <p>{ex}</p>...')
    
def ask_gigachat(system_text, user_text):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    payload = json.dumps({
    "model": "GigaChat",
    "messages": [
      {
      "role": "system",
      "content": system_text,
    },
    {
      "role": "user",
      "content": user_text,
    }
    ],
    "stream": False,
    "update_interval": 0
    })

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {ACCESS_TOKEN}'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as ex:
        return HttpResponse(f'Произошла ошибка: <p>{ex}</p>...')