import requests

headers = {
    'authority': 'my.fora.ua',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': '*/*',
    'access-token': 'NWRjMzBkODBkOGZjYTM4OWQwY2QyOTczZTQ5NGRhNTg',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://fora.ua',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://fora.ua/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = '{"operationName":"me","variables":{},"query":"query me {\\n  me {\\n    ...UserFragment\\n    __typename\\n  }\\n  getPickUpList {\\n    filialId\\n    deliveryServiceId\\n    __typename\\n  }\\n}\\n\\nfragment UserFragment on User {\\n  id\\n  firstName\\n  lastName\\n  middleName\\n  fullPhoneNumber\\n  email\\n  emailConfirmed\\n  currentBonus\\n  currentBalance\\n  notification\\n  barcode\\n  bonusAmount\\n  vouchersAmount\\n  spawnNextCouponDate\\n  __typename\\n}\\n"}'

response = requests.post('https://my.fora.ua/graphql', headers=headers, data=data)
