from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def set_chrome_options():
    # path_chrome = 'bin/google-chrome'
    chrome_options = Options()
    #Запуск без графического интерфейса
    chrome_options.add_argument("--headless")
    #Обход модели безопасности
    chrome_options.add_argument("--no-sandbox")
    #преодолеть проблемы с ограниченными ресурсами
    chrome_options.add_argument("--disable-dev-shm-usage")
    #Установка разрешения экрана
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

if __name__== '__main__':
    webdriver = webdriver.Chrome(options=set_chrome_options())
    webdriver.get('https://www.google.com/')
    webdriver.save_screenshot('screen.png')
    print('Hello')
    webdriver.close()
