import allure
import pytest
from base.base_class import Base
from pages.some_page import SomePage
from pages.authorizationpage import AuthorizationPage

base = Base()
auth = AuthorizationPage()
some = SomePage()

PASSWORD = 'test'
EMAIL = 'test@protei.ru'
NAME = 'Boris Pulia'
EMAIL_ALERT_MESSAGE = 'Неверный формат E-Mail'
NAME_ALERT_MESSAGE = 'Поле имя не может быть пустым'
INVALID_EMAIL = ['test@proteiru', 'test', 'test_protei.ru', '/^[^-]+?@.+?$/', '']
INVALID_NAME = ['1234', '/^[^-]+?@.+?$/', '', '   ']

@allure.description('Smoke проверка формы')
@pytest.mark.run(ordering=4)
def test_form():
    some.input_email(EMAIL)
    some.input_name(NAME)
    some.select_gender_woman()
    some.click_var11_checkbox()
    some.click_var22_radio_button()
    some.click_add_button()
    some.click_modal_window_button()
    some.check_field_table(EMAIL)
    some.check_field_table(NAME)
    some.check_field_table('Женский')
    some.check_field_table('1.1')
    some.check_field_table('2.2')

@allure.description('Проверка реакции поля E-Mail на невалидные значения')
@pytest.mark.run(ordering=5)
@pytest.mark.parametrize('data', INVALID_EMAIL)
def test_email_field(data):
    some.input_email(data)
    some.input_name(NAME)
    some.click_add_button()
    try:
        some.get_alerts_email_messages()
    except:
        assert some.click_modal_window_button(), 'FALSE___Alert message is not triggered'
    assert some.get_alerts_email_messages() == EMAIL_ALERT_MESSAGE, \
        f'FALSE___Call messages {some.get_alerts_email_messages()}, expected {EMAIL_ALERT_MESSAGE}'

@allure.description('Проверка реакции поля Имя на невалидные значения')
@pytest.mark.run(ordering=6)
@pytest.mark.parametrize('data', INVALID_NAME)
def test_name_field(data):
    some.input_email(EMAIL)
    some.input_name(data)
    some.click_add_button()
    try:
        some.get_alerts_name_messages()
    except:
        assert some.click_modal_window_button(), 'FALSE___Alert message is not triggered'
    assert some.get_alerts_name_messages() == NAME_ALERT_MESSAGE, \
        f'FALSE___Call messages {some.get_alerts_name_messages()}, expected {NAME_ALERT_MESSAGE}'

@allure.description('Проверка включения и отключения радиокнопок')
@pytest.mark.run(ordering=7)
def test_radio_button():
    some.checking_status_change_radiobutton()


