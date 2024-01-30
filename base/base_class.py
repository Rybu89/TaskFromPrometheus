import os
import pickle

from base.driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class Base(Driver):
    def open_page(self, url):
        """ Открытие страницы"""

        self.browser.get(url)
        print('___Open page: ' + url)

    def _get_present_element(self, element_locator):
        """ Метод получения элемента по его локатору.
                Принимает:
                 element_locator - локатор элемента
        """

        return WebDriverWait(self.browser, 3).until(ec.presence_of_element_located(element_locator))

    def _click_clickable_element(self, element_locator):
        """ Метод нажатия на элемент.
                Принимает:
                 element_locator - локатор элемента
        """

        WebDriverWait(self.browser, 3).until(ec.element_to_be_clickable(element_locator)).click()

    def _get_clickable_element(self, element_locator):
        """ Метод получения кликабельного элемента по его локатору.
                Принимает:
                 element_locator - локатор элемента
        """

        return WebDriverWait(self.browser, 3).until(ec.element_to_be_clickable(element_locator))

    def _save_cookies(self, name_file_cookie):

        """ Метод для записи cookies.
                Принимает:
                   name_file_cookie - имя сохраняемого файла (Str)
        """

        print('\n Запись cookies')
        pickle.dump(self.browser.get_cookies(), open(os.getcwd() + '\\cookies\\' + f"{name_file_cookie}_cookies", "wb"))
        print('\n Cookies записаны')

    def _load_cookies(self, name_file_cookie):

        """ Метод для загрузки cookies.
                Принимает:
                   name_file_cookie - имя загружаемого файла (Str)
        """

        print('\n Загрузка cookies')
        for cookie in pickle.load(open(os.getcwd() + '\\cookies\\' + f"{name_file_cookie}_cookies", "rb")):  #
            self.browser.add_cookie(cookie)
        self.browser.refresh()
        print('\n Cookies загружены')

    def _get_select_element(self, element_locator):

        return Select(self.browser.find_element(*element_locator))

    def _get_text(self, element_locator):

        return WebDriverWait(self.browser, 3).until(ec.visibility_of_element_located(element_locator)).text

