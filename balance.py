import requests, json, os, importlib
from barcoder import decoder
import os.path

directory = 'numbbers/'     
files = list(os.listdir(directory))
files.remove("__init__.py")
files.remove("__pycache__")

def all_the_number(texts, n):
    if ' ' in texts and texts.replace(' ', '').isdigit():
        elements = texts.split(" ")
    elif texts.isdigit():
        elements = [texts]
    else:
        print(texts + ' is not numbers')
        return False
    status = True
    for one in elements:
        if one.isdigit() == False:
            status = False
        elif int(one) >= n or int(one) < 0:
            status = False
    return status

def all_0():
    str_0 = ''
    for name in files:
        
        info = json_result(name)
        str_0 += str(info) + '\n'
    return str_0

def all_1(texts):
    all_indexs = texts.split(" ")
    str_1 = ''
    for n in all_indexs:
        
        info = json_result(files[int(n)])
        print(info)
        str_1 += str(info) + '\n'
    return str_1

def all_numbers():
    inx = 0
    all_numbers = ''
    for i in files:
        name = i.split(".")[0]
                
        all_numbers += ' {0} - <b>{1}</b>\n'.format(str(inx), name)    # + " - " + name + '\n')
        inx += 1
    return all_numbers

def json_result(name):
    plugin_name = directory[:-1] + '.' + name.split(".")[0]
    module = importlib.import_module(plugin_name, '.')
    text = module.response.json()

    barcode = str(text['data']['me']["barcode"])
    currentBalance = int(text['data']['me']["currentBalance"])
    currentBonus = round(float(text['data']['me']["currentBonus"]), 2)
    email = str(text['data']['me']["email"])
    info_dict = {
        'barcode': barcode, 
        'number': str(name.split(".")[0]),
        'bonus': currentBalance,
        'balance': currentBonus,
        'email': email,
    }
    # decoder(info_dict['number'], barcode)
    return info_dict

if  __name__ == "__main__":
    while True:
        indx = str(input(
        """Эта программа проверяет информацию
об аккаунте в приложении \"Fora\"
    ---
Сколько аккаунтов проверить?
(0 - все; 1 - несколько)
--- """))
        if indx.isdigit():
            if int(indx) != 0 and int(indx) != 1:
                continue
        else:
            continue

        indx = int(indx)
        
        if indx == 0:
            print(all_0())
        elif indx == 1:
            inx = 0
            print(all_numbers())
            
            all_indexs = str(input("Какие номера проверить?\n(Напишите в таком формате - \"0 1 2\")\n---"))
            status = all_the_number(all_indexs, len(files))
            if status == False:
                while status == False:
                    print("Ошибка в написании \n(возможно какой-то номер слишком большой)! \nПопробуйте снова\n")
                    all_indexs = str(input("Какие номера проверить?\n(Напишите в таком формате - \"0 1 2\")\n---")).split(" ")
                    status = all_the_number(all_indexs, len(files))
                    
            all_1(all_indexs)

