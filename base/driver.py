from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class Driver:

    options = webdriver.ChromeOptions()
    ''' Создание объекта класса ChromeOptions '''
    options.add_experimental_option("detach", True)
    ''' Подключение опции - оставить браузер открытым в конце сессии '''
    options.add_argument("--incognito")
    ''' Подключение опции - открыть браузер в режиме инкогнито '''
    options.add_argument("--disable-cache")
    ''' Подключение опции - отменить загрузку кеша '''
    options.add_argument("--window-size=1920,1080")
    ''' Подключение опции - открывать окно браузера в разрешении 1920х1080 '''
    # options.page_load_strategy = "eager"
    ''' Подключение стратегии загрузки страницы - не ожидать полной отрисовки страниц '''
    # options.add_argument("--headless")
    ''' Подключение опции - запуск драйвера без графического отображения (безголовый режим) '''
    options.add_argument("--disable-blink-features=AutomationControlled")
    s = Service()
    browser = webdriver.Chrome(options=options, service=s)
