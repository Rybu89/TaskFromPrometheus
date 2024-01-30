import allure

from base.base_class import Base


class SomePage(Base):

    def __init__(self):
        super().__init__()

    url = 'file:///C:/Users/79531/Downloads/qa-test%20(2).html'

    # Locators
    locator_email_title = ["xpath", '//label[@for="dataEmail" and contains(text(), "E-Mail")]']
    locator_email_field = ["xpath", '//input[@id="dataEmail"]']
    locator_name_title = ["xpath", '//label[@for="dataName"]']
    locator_name_field = ["xpath", '//input[@id="dataName"]']
    locator_gender_title = ["xpath", '//label[@for="dataGender"]']
    locator_gender_select = ["xpath", '//select[@id="dataGender"]']
    locator_var11_checkbox = ["xpath", '//input[@id="dataCheck11"]']
    locator_var12_checkbox = ["xpath", '//input[@id="dataCheck12"]']
    locator_radio_buttons = ["xpath", '(//input[@type="radio"])']
    locator_var21_radio_button = ["xpath", '//input[@id="dataSelect21"]']
    locator_var22_radio_button = ["xpath", '//input[@id="dataSelect22"]']
    locator_var23_radio_button = ["xpath", '//input[@id="dataSelect23"]']
    locator_add_button = ["xpath", '//button[@id="dataSend"]']
    locator_alerts_email_messages = ["xpath", '//div[@id="emailFormatError"]']
    locator_alerts_name_messages = ["xpath", '//div[@id="blankNameError"]']
    locator_modal_window_button = ["xpath", '//button[@class="uk-button uk-button-primary uk-modal-close"]']
    locator_field_table = ["xpath", '//tbody//tr']

    # Getters
    def get_alerts_email_messages(self):
        text_error = self._get_present_element(self.locator_alerts_email_messages).text
        return text_error

    def get_alerts_name_messages(self):
        text_error = self._get_present_element(self.locator_alerts_name_messages).text
        return text_error

    def get_var21_radio_button(self):
        return self._get_present_element(self.locator_var21_radio_button)

    def get_var22_radio_button(self):
        return self._get_present_element(self.locator_var22_radio_button)

    def get_field_table(self):
        return self._get_text(self.locator_field_table)

    def get_status_radiobutton(self, radio_button):
        """ Получить текущее состояние переключателя.
                Возвращает:
                    False - в случае, если переключатель не выбран;
                    True - в случае, если переключатель выбран.
        """
        return self._get_clickable_element(radio_button).is_selected()

    # Actions
    def input_email(self, email):
        with allure.step('Input email.'):
            self._get_clickable_element(self.locator_email_field).clear()
            self._get_clickable_element(self.locator_email_field).send_keys(email)
            print("\n___Input email: " + email)

    def input_name(self, name):
        with allure.step('Input name.'):
            self._get_present_element(self.locator_name_field).clear()
            self._get_present_element(self.locator_name_field).send_keys(name)
            print("\n___Input name: " + name)

    def select_gender_man(self):
        with allure.step('Select gender man.'):
            self._get_select_element(self.locator_gender_select).select_by_visible_text('Мужской')
            print("\n___Select gender man.")
    def select_gender_woman(self):
        with allure.step('Select gender woman.'):
            self._get_select_element(self.locator_gender_select).select_by_visible_text('Женский')
            print("\n___Select gender woman.")

    def click_add_button(self):
        with allure.step('Click Add button.'):
            self._click_clickable_element(self.locator_add_button)
            print("\n___Click Add button.")

    def click_modal_window_button(self):
        with allure.step('Click Ok in button modal window.'):
            self._click_clickable_element(self.locator_modal_window_button)
            print("\n___Click Ok in button modal window.")

    def click_var11_checkbox(self):
        with allure.step('Click checkbox Вариант 1.1.'):
            self._click_clickable_element(self.locator_var11_checkbox)
            print("\n___Click checkbox Вариант 1.1.")

    def click_var21_radio_button(self):
        with allure.step('Click radio_button Вариант 2.1.'):
            self._click_clickable_element(self.locator_var21_radio_button)
            print("\n___Click radio_button Вариант 2.1.")
    def click_var22_radio_button(self):
        with allure.step('Click radio_button Вариант 2.2.'):
            self._click_clickable_element(self.locator_var22_radio_button)
            print("\n___Click radio_button Вариант 2.2.")

    # Methods

    def checking_status_change_radiobutton(self):
        with allure.step('Checking status change radiobutton'):
            default_status = self.get_var21_radio_button().is_selected()
            self.click_var21_radio_button()
            after_on = self.get_var21_radio_button().is_selected()
            assert default_status is False and after_on is True, 'FALSE___ Radio button not clickable'
            self.click_var22_radio_button()
            status_off = self.get_var21_radio_button().is_selected()
            assert after_on is True and status_off is False, 'FALSE___ Radio button not off'
            print('___Checking default status radiobuttons. __PASSED')
            print('___Checking status change radiobuttons. __PASSED')

    def check_field_table(self, expected_value):
        act_value = self.get_field_table()
        assert expected_value in act_value, f'FALSE___ В таблицу добавлены неверные значения: {act_value}'
