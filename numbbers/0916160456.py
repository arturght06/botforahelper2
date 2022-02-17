import requests

headers = {
    'authority': 'my.fora.ua',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'x-correlation-id': '0efea1c4-67d9-b9f1-393e-225d352b4d9a',
    'sec-ch-ua-mobile': '?0',
    'access-token': 'OGQzZDc2NjU5Y2VlMmI3OWQ4OTkxNTgzZTVkM2M4M2Q',
    'content-type': 'application/json',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'x-request-id': 'd5d70fac-5fc0-2571-12c1-91a5e0b5e32c',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://my.fora.ua',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://my.fora.ua/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
}

data = '{"operationName":"me","variables":{},"query":"query me {\\n  me {\\n    ...UserFragment\\n    __typename\\n  }\\n}\\n\\nfragment UserFragment on User {\\n  id\\n  firstName\\n  lastName\\n  middleName\\n  email\\n  emailConfirmed\\n  currentBonus\\n  currentBalance\\n  notification\\n  barcode\\n  spawnNextCouponDate\\n  __typename\\n}\\n"}'

response = requests.post('https://my.fora.ua/graphql', headers=headers, data=data)
