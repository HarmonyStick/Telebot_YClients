# -*- coding: utf8 -*-
# !/usr/local/bin/python3

import sys
import json
import os.path
import requests
import datetime
import telebot
import difflib as df

bot = telebot.TeleBot('api-ключ для телеграм-бота')

# Авторизация пользователя в системе YClients
values = """
  {
	"login": "логин",
	"password": "пароль"
  }
"""

# API-ключ
bearer = Bearer 'API-ключ для YClients'

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.yclients.v2+json',
    'Authorization': bearer
}

s = requests.Session()
page = s.post("https://api.yclients.com/api/v1/auth", data=values, headers=headers)

# Получение User-token
response_body = page.text
response_body = json.loads(response_body)
UserToken = response_body['data']['user_token']

# Вставляем User-token в запрос на получение всех записей
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.yclients.v2+json',
    'Authorization': bearer + ',' + UserToken
}

# Запрос на все записи на сегодняшнее число
# date = datetime.date.today()
# date = str(date)
# c = requests.Session()
# request = c.get('https://api.yclients.com/api/v1/records/'id_мастера'?start_date=' + date + '&end_date=' + date, headers=headers)

# Запрос на все записи с сегодняшнего дня до конкретного числа
date = datetime.date.today()
# date_1 = datetime.datetime.strptime(start_date, "%m/%d/%y")
end_date = date + datetime.timedelta(days=14)
date = str(date)
end_date = str(end_date)
c = requests.Session()
request = c.get('https://api.yclients.com/api/v1/records/'id_мастера'?start_date=' + date + '&end_date=' + end_date,
                headers=headers)
# request = c.get('https://api.yclients.com/api/v1/records/'id_мастера'?start_date=2021-01-18&end_date=2021-01-23', headers=headers)


# Получаем необходимые параметры из ответа
response_body = request.text
response_body = json.loads(response_body)
data = response_body['data']
records = 0

if os.path.exists('test.txt'):
    f = open("test2.txt", "w")
    for elem in data:
        try:
            client_name = elem['client']['name']
            print(client_name, file=f)
        except:
            print('Без имени', file=f)
        try:
            title = elem['services'][0]['title']
            print(title, file=f)
        except:
            print('Услуга не определена', file=f)
        client_date = elem['date']
        print(client_date, file=f)
        print('', file=f)
        records += 1
    f.close()

else:
    f = open("test.txt", "w")
    for elem in data:
        try:
            client_name = elem['client']['name']
            print(client_name, file=f)
        except:
            print('Без имени', file=f)
        try:
            title = elem['services'][0]['title']
            print(title, file=f)
        except:
            print('Услуга не определена', file=f)
        client_date = elem['date']
        print(client_date, file=f)
        print('', file=f)
        records += 1
    f.close()

test = open('test.txt', 'r')
test2 = open('test2.txt', 'r')

string = ''

date = datetime.datetime.today()
my_date = date.strftime('%H:%M')
if my_date != '00:00':
    # Записываем количество записей в файл
    # Если файл существует, то считываем число из файла и сравниваем его с количеством записей
    def send_message():
        bot.send_message('id_чата', string)


    if os.path.exists('file.txt'):
        f = open('file.txt', 'r')
        old_records = f.readline()
        old_records = int(old_records)
        if records > old_records:
            string = 'У вас новая запись!'
            records = str(records)
            f = open('file.txt', 'w')
            f.write(records)
            f.close()

            d = df.Differ()
            diff = d.compare(test.readlines(), test2.readlines())

            test3 = open('test3.txt', 'w')
            test3.write(''.join(diff))
            test3.close()

            test3 = open('test3.txt', 'r')
            s = test3.readlines()

            orig_stdout = sys.stdout
            test4 = open('test4.txt', 'w')
            sys.stdout = test4

            for i in s:
                if i[0] == '+':
                    print(i[2:], end='')

            sys.stdout = orig_stdout
            test4.close()

            with open(r"test4.txt", "r") as file:
                for line in file:
                    string = line + string + '\n'
            if __name__ == '__main__':
                send_message()

            f = open("test.txt", "w")
            for elem in data:
                try:
                    client_name = elem['client']['name']
                    print(client_name, file=f)
                except:
                    print('Без имени', file=f)
                try:
                    title = elem['services'][0]['title']
                    print('Услуга не определена', file=f)
                client_date = elem['date']
                print(client_date, file=f)
                print('', file=f)
            f.close()

                    print(title, file=f)
                except:


        elif records < old_records:
            string = 'Запись отменена!'
            records = str(records)
            f = open('file.txt', 'w')
            f.write(records)
            f.close()

            d = df.Differ()
            diff = d.compare(test2.readlines(), test.readlines())

            test3 = open('test3.txt', 'w')
            test3.write(''.join(diff))
            test3.close()

            test3 = open('test3.txt', 'r')
            s = test3.readlines()

            orig_stdout = sys.stdout
            test4 = open('test4.txt', 'w')
            sys.stdout = test4

            for i in s:
                if i[0] == '+':
                    print(i[2:], end='')

            sys.stdout = orig_stdout
            test4.close()

            with open(r"test4.txt", "r") as file:
                for line in file:
                    string = line + string + '\n'
            if __name__ == '__main__':
                send_message()

            f = open("test.txt", "w")
            for elem in data:
                try:
                    client_name = elem['client']['name']
                    print(client_name, file=f)
                except:
                    print('Без имени', file=f)
                try:
                    title = elem['services'][0]['title']
                    print(title, file=f)
                except:
                    print('Услуга не определена', file=f)
                client_date = elem['date']
                print(client_date, file=f)
                print('', file=f)
            f.close()


        elif records == old_records:
            f = open("test.txt", "w")
            for elem in data:
                try:
                    client_name = elem['client']['name']
                    print(client_name, file=f)
                except:
                    print('Без имени', file=f)
                try:
                    title = elem['services'][0]['title']
                    print(title, file=f)
                except:
                    print('Услуга не определена', file=f)
                client_date = elem['date']
                print(client_date, file=f)
                print('', file=f)
            f.close()



    # Если файл не существует, то создаем его и записываем количество записей в него
    else:
        records = str(records)
        f = open('file.txt', 'w')
        f.write(records)
        f.close()
else:
    records = str(records)
    f = open('file.txt', 'w')
    f.write(records)
    f.close()
