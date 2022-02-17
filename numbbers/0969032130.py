import requests

headers = {
    'authority': 'my.fora.ua',
    'accept': 'application/json',
    'x-correlation-id': 'df1998d7-e6cf-bd41-1916-1edb8728e5fe',
    'content-type': 'application/json',
    'access-token': 'MDQzMjJmMzQ3MGI1NmI2YmM1MDdiNWQ3M2E2YmViNWE',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'x-request-id': '1401b560-8bd0-5109-ff03-e710d9121ef4',
    'origin': 'https://my.fora.ua',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://my.fora.ua/',
    'accept-language': 'ru,en-UA;q=0.9,en;q=0.8,ru-UA;q=0.7,en-US;q=0.6,uk;q=0.5,pl;q=0.4',
}

data = '{"operationName":"me","variables":{},"query":"query me {\\n  me {\\n    ...UserFragment\\n    __typename\\n  }\\n}\\n\\nfragment UserFragment on User {\\n  id\\n  firstName\\n  lastName\\n  middleName\\n  email\\n  emailConfirmed\\n  currentBonus\\n  currentBalance\\n  notification\\n  barcode\\n  spawnNextCouponDate\\n  __typename\\n}\\n"}'

response = requests.post('https://my.fora.ua/graphql', headers=headers, data=data)

