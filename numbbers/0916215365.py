import requests

headers = {
    'authority': 'my.fora.ua',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'x-correlation-id': 'f7670800-d09b-3bb0-1b6a-b1d61d1c32f9',
    'sec-ch-ua-mobile': '?0',
    'access-token': 'YjM3MTliMzE3YTA4ZTg3ZTU5MjgzZmI4YWE3NjAwNjY',
    'content-type': 'application/json',
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'x-request-id': 'e1c1bb41-c952-7623-1872-a02a8f81e1cb',
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
