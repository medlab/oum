from selenium.webdriver.common import by
from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from .import uiacontractfortest
from ..oum import OUMElement, auto_set_all_oum_element_driver_attr

class OUMTestWpfApp:
    txt_name_holder_element = OUMElement(None, find_by=by.By.ID, by_value=uiacontractfortest.OUM_TESTWPFAPP_EXE_PATH_AUID_BTN_OPEN_NAME_HOLDER)
    def __init__(self, driver):
        '''

        :param driver:
        :type driver: WebDriver
        '''
        auto_set_all_oum_element_driver_attr(self, driver)
        pass
    pass