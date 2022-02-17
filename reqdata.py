import requests
import json

# Эта функция получает основную инфу об аккаунте  по токену
def req(acstkn):
    headers = {
    'authority': 'my.fora.ua',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'x-correlation-id': '3b279e4e-185b-ff81-059c-d3129d1de588',
    'sec-ch-ua-mobile': '?0',
    'access-token': acstkn,
    'content-type': 'application/json',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'x-request-id': '12e4000b-a751-b16c-4df1-6982dcec34f6',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://my.fora.ua',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://my.fora.ua/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}

    data1 = '{"operationName":"me","variables":{},"query":"query me {\\n  me {\\n    ...UserFragment\\n  }\\n}\\n\\nfragment UserFragment on User {\\n  currentBonus\\n  currentBalance\\n  barcode\\n}\\n"}'
    data2 = '{"operationName":"meDetailed","variables":{},"query":"query meDetailed {\\n  me: meDetailed {\\n    ...DetailedUserFragment\\n  }\\n}\\n\\nfragment DetailedUserFragment on DetailedUser {\\n  mobilePhoneCode\\n  mobilePhoneNumber\\n}\\n"}'
    try:
        response_number = requests.post('https://my.fora.ua/graphql', headers=headers, data=data2)
        mobilePhoneCode = response_number.json()["data"]["me"]["mobilePhoneCode"]
        mobilePhoneNumber = response_number.json()["data"]["me"]["mobilePhoneNumber"]
        phone_number = mobilePhoneCode + mobilePhoneNumber

        response_info = requests.post('https://my.fora.ua/graphql', headers=headers, data=data1)
        currentBonus = response_info.json()['data']['me']['currentBonus']
        currentBalance = response_info.json()['data']['me']['currentBalance']
        barcode = response_info.json()['data']['me']['barcode']

        data = {'phone_number': str(phone_number), 'currentbonus': str(currentBonus), 'currentbalance': str(currentBalance), 'barcode': str(barcode) }
        return data
    except:
        response_info = requests.post('https://my.fora.ua/graphql', headers=headers, data=data1)
        if 'errors' in response_info.text:
            return 'Ключ устарел'
        return False

# print(req("OGQzZDc2NjU5Y2VlMmI3OWQ4OTkxNTgzZTVkM2M4M2Q"))

    
