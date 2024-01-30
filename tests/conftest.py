import pytest
from base.base_class import Base
from base.driver import Driver
from pages.authorizationpage import AuthorizationPage
from pages.some_page import SomePage


base = Base()
auth = AuthorizationPage()
some = SomePage()
dr = Driver()
@pytest.fixture(scope="session")
def from_auth():

    print('\nSTART')
    base.open_page(auth.url)
    yield
    # dr.browser.quit()
    print('\nFINISH')

# @pytest.fixture(scope="session")
# def from_some():
#
#     print('\nSTART')
#     base.open_page(some.url)
#     base._load_cookies("second")
#
#     yield
#     dr.browser.quit()
#     print('\nFINISH')
