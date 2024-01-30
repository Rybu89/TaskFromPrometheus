from base.base_class import Base

class AuthorizationPage(Base):

    def __init__(self):
        super().__init__()

    url = 'file:///C:/Users/79531/Downloads/qa-test%20(2).html'

    # Locators
    locator_email_title = ["xpath", '//label[@for="loginEmail" and contains(text(), "E-Mail")]']
    locator_email_field = ["xpath", '//input[@id="loginEmail"]']
    locator_password_title = ["xpath", '//label[@for="loginPassword"]']
    locator_password_field = ["xpath", '//input[@id="loginPassword"]']
    locator_input_button = ["xpath", '//button[@id="authButton"]']
    locator_alerts_messages = ["xpath", '//div[@id="authAlertsHolder"]']

    # Getters
    def get_alert_message(self):
        try:
            text_error = self._get_present_element(self.locator_alerts_messages).text
            return text_error
        except:
            return False

    # Actions
    def input_email(self, email):
        """  Ввод в поле - E-Mail. """

        self._get_clickable_element(self.locator_email_field).clear()
        self._get_clickable_element(self.locator_email_field).send_keys(email)
        print("\n___Input email: " + email)

    def input_password(self, password):
        """  Ввод в поле - Пароль. """

        self._get_present_element(self.locator_password_field).clear()
        self._get_present_element(self.locator_password_field).send_keys(password)
        print("\n___Input password: " + password)

    def click_input_button(self):
        """  Клик по кнопке - Вход. """

        self._click_clickable_element(self.locator_input_button)
        print("\n___Click input button.")

    # Methods
