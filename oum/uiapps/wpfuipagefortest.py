from selenium.webdriver.common import by
from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from .import uiacontractfortest
from ..oum import OUMElement, auto_set_all_oum_element_driver_attr, SeleniumElementProxy, SeleniumElementProxyBase, create_subtree_element_under_driver_context, SeleniumSubTreeProxyBase


class OUMTestWpfApp(SeleniumSubTreeProxyBase):
    txt_name_holder_element = OUMElement(None, find_by=by.By.ID, by_value=uiacontractfortest.OUM_TESTWPFAPP_AUID_BTN_OPEN_NAME_HOLDER)
    pass

class OUMTestWpfAppContainer: # TODO should be mark with top level windows uid?
    def __init__(self, driver):
        # container_element=SeleniumElementProxy(find_by=by.By.ID, by_value=uiacontractfortest.OUM_TESTWPFAPP_AUID_WINDOW_MAINWINDOW)
        # container_element.driver=driver
        # container_element.parent_selenium_element_proxy=None
        #
        # self.holder_element=container_element
        #
        # self.main_page=OUMTestWpfApp(driver, self.holder_element)
        subtree_element=create_subtree_element_under_driver_context(driver,find_by=by.By.ID, by_value=uiacontractfortest.OUM_TESTWPFAPP_AUID_WINDOW_MAINWINDOW) # type: SeleniumSubTreeProxyBase
        subtree_element.init_context(driver, None)
        self.main_page=subtree_element

        pass
    pass