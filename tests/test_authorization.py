import pytest
from base.base_class import Base
from pages.authorizationpage import AuthorizationPage
import allure

base = Base()
auth = AuthorizationPage()

EMAIL = 'test@protei.ru'
PASSWORD = 'test'
EMAIL_ALERT_MESSAGE = 'Неверный формат E-Mail'
PASSWORD_ALERT_MESSAGE = 'Неверный E-Mail или пароль'
INVALID_EMAIL = ['test', 'test_protei.ru', 'test@proteiru', '']
INVALID_PASSWORD = ['1234', 'TEST', '']

@allure.description('Проверка реакции поля email на невалидные значения')
@pytest.mark.run(ordering=1)
@pytest.mark.parametrize('data', INVALID_EMAIL)
def test_email_field(from_auth, data):
    auth.input_email(data)
    auth.input_password(PASSWORD)
    auth.click_input_button()
    act_message = auth.get_alert_message()
    try:
        act_message
    except:
        assert 'FALSE___Alert messages not found'

    assert act_message == EMAIL_ALERT_MESSAGE, f'FALSE___Call messages {act_message}, expected {EMAIL_ALERT_MESSAGE}'

@allure.description('Проверка реакции поля password на невалидные значения')
@pytest.mark.run(ordering=2)
@pytest.mark.parametrize('data', INVALID_PASSWORD)
def test_password_field(data):
    auth.input_email(EMAIL)
    auth.input_password(data)
    auth.click_input_button()
    act_message = auth.get_alert_message()
    try:
        act_message
    except:
        assert 'FALSE___Alert messages not found'

    assert act_message == PASSWORD_ALERT_MESSAGE, f'FALSE___Call messages {act_message}, expected ' \
                                                  f'{PASSWORD_ALERT_MESSAGE}'

@allure.description('Авторизация')
@pytest.mark.run(ordering=3)
def test_authorization(from_auth):
    auth.input_email(EMAIL)
    auth.input_password(PASSWORD)
    auth.click_input_button()
    # base._save_cookies("second")
