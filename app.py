# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
import os
import time
import datetime
from exchangelib import Credentials, Account, Configuration, DELEGATE, IMPERSONATION, Message, Mailbox

# def set_chrome_options():
#     # path_chrome = 'bin/google-chrome'
#     chrome_options = Options()
#     #Запуск без графического интерфейса
#     chrome_options.add_argument("--headless")
#     #Обход модели безопасности
#     chrome_options.add_argument("--no-sandbox")
#     #преодолеть проблемы с ограниченными ресурсами
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     #Установка разрешения экрана
#     chrome_options.add_argument("--window-size=1920x1080")
#     chrome_prefs = {}
#     chrome_options.experimental_options["prefs"] = chrome_prefs
#     chrome_prefs["profile.default_content_settings"] = {"images": 2}
#     return chrome_options

if __name__== '__main__':
    # webdriver = webdriver.Chrome(options=set_chrome_options())
    # webdriver.get('https://www.google.com/')
    # webdriver.save_screenshot('source/screen/screen.png')
    # webdriver.close()
    # # path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'attach/readme.txt')
    # # if os.path.isfile('/home/serj52/PycharmProjects/docker_work/attach/readme.txt'):
    # with open('source/input.txt') as file:
    #     print(file.read())
    # with open('source/readme.txt') as file:
    #     print(file.read())

    server = 'mail.rosatom.ru'
    email = 'GREN-r-000004@Greenatom.ru'
    name = r'gk\GREN-r-000004'
    password = 'Bayern2025'
    credentials = Credentials(name, password)
    config = Configuration(server=server, credentials=credentials)
    account = Account(primary_smtp_address=email, config=config, credentials=credentials, autodiscover=True, access_type=DELEGATE)

    count = 1
    # Печать входящих сообщений
    # for item in account.inbox.all().order_by('-datetime_received')[:10]:
    #     #{item.sender}, {item.datetime_received}
    #     print(f'{count}. {item.subject}')

    #Отправка сообщений
    m = Message(account=account,
                subject='Тест',
                body='Тестовое сообщение от робота',
                to_recipients=[Mailbox(email_address='blackday52@mail.ru'),])
    m.send()
