import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
import unittest

from oum.oum import SeleniumElementProxyBase, SeleniumElementProxy
from ..uiapps import uiacontractfortest, wpfuipagefortest

class BaseUiTestCase(unittest.TestCase):
    def setUp(self):
        # put it in setUp
        self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                  desired_capabilities={
                                      #'debugConnectToRunningApp': 'true',
                                      'debugConnectToRunningApp': 'false',
                                      'app': uiacontractfortest.OUM_TESTWPFAPP_EXE_PATH,
                                      'args': ''})
        pass

    def tearDown(self):
        self.driver.close()
        pass

class BasicSeleniumElementRetrieveAndPropertyAcessTestCase(BaseUiTestCase):
    def test_get_one_by_id(self):
        txt_name_holder_element=self.driver.find_element(by=by.By.ID, value=uiacontractfortest.OUM_TESTWPFAPP_AUID_BTN_OPEN_NAME_HOLDER)
        actual_value=txt_name_holder_element.text
        expect_value=uiacontractfortest.OUM_TESTWPFAPP_ADEFAULTVALUE_BTN_OPEN_NAME_HOLDER
        self.assertEqual(expect_value, actual_value)

        txt_name_holder_element.click() # TODO it not work here!

        new_content="hello world"
        txt_name_holder_element.clear()
        txt_name_holder_element.send_keys(new_content)
        actual_value=txt_name_holder_element.text
        expect_value=new_content
        self.assertEqual(expect_value, actual_value)

        pass

    def test_get_one_by_id_by_directly_oum_proxy_object(self):
        txt_name_holder_element= SeleniumElementProxy(find_by=by.By.ID,
                                                      by_value=uiacontractfortest.OUM_TESTWPFAPP_AUID_BTN_OPEN_NAME_HOLDER)  # type: WebElement | SeleniumElementProxyBase

        txt_name_holder_element.driver=self.driver

        actual_value=txt_name_holder_element.text
        expect_value=uiacontractfortest.OUM_TESTWPFAPP_ADEFAULTVALUE_BTN_OPEN_NAME_HOLDER
        self.assertEqual(expect_value, actual_value)

        txt_name_holder_element.click() # TODO it not work here!

        new_content="hello world"
        txt_name_holder_element.clear()
        txt_name_holder_element.send_keys(new_content)
        actual_value=txt_name_holder_element.text
        expect_value=new_content
        self.assertEqual(expect_value, actual_value)

        pass

    def test_get_one_by_id_by_oum_element_pd_in_page_obj(self):
        wpf_test_app=wpfuipagefortest.OUMTestWpfApp(self.driver)

        txt_name_holder_element=wpf_test_app.txt_name_holder_element

        actual_value = txt_name_holder_element.text
        expect_value = uiacontractfortest.OUM_TESTWPFAPP_ADEFAULTVALUE_BTN_OPEN_NAME_HOLDER
        self.assertEqual(expect_value, actual_value)

        txt_name_holder_element.click()  # TODO it not work here!

        new_content = "hello world"
        txt_name_holder_element.clear()
        txt_name_holder_element.send_keys(new_content)
        actual_value = txt_name_holder_element.text
        expect_value = new_content
        self.assertEqual(expect_value, actual_value)

        pass

    def test_get_one_by_id_by_oum_element_pd_in_page_obj_in_container_page_obj(self):
        main_window_container=wpfuipagefortest.OUMTestWpfAppContainer(self.driver)

        wpf_test_app=main_window_container.main_page

        txt_name_holder_element=wpf_test_app.txt_name_holder_element

        actual_value = txt_name_holder_element.text
        expect_value = uiacontractfortest.OUM_TESTWPFAPP_ADEFAULTVALUE_BTN_OPEN_NAME_HOLDER
        self.assertEqual(expect_value, actual_value)

        txt_name_holder_element.click()  # TODO it not work here!

        new_content = "hello world"
        txt_name_holder_element.clear()
        txt_name_holder_element.send_keys(new_content)
        actual_value = txt_name_holder_element.text
        expect_value = new_content
        self.assertEqual(expect_value, actual_value)

        pass

    def test_property_access(self):
        pass

    def test_get_many_by_id(self):
        pass

    def test_get_one_by_name(self):
        pass

    def test_get_many_by_name(self):
        pass

    def test_get_one_by_xpath(self):
        pass

    def test_get_many_by_xpath(self):
        pass

    pass


class BasicOUMDriveElementRetrieveAndPropertyAcessTestCase(BaseUiTestCase):
    def test_element_mark_by_id(self):
        pass

    def test_property_access(self):
        pass

    def test_elements_mark_by_id(self):
        pass

    def test_element_mark_by_name(self):
        pass

    def test_elements_mark__by_name(self):
        pass

    def test_element_mark_by_xpath(self):
        pass

    def test_elements_mark_by_xpath(self):
        pass
    pass


class AdvanceOUMDriveElementRetrieveAndPropertyAcessTestCase(BaseUiTestCase):
    def test_lazy_element_mark_by_id(self):
        pass

    def test_property_access(self):
        pass

    def test_dirty_element_mark_by_id(self):
        pass

    def test_dynamic_and_dirty_subtree_elements_mark_by_id_(self):
        pass


if __name__ == '__main__':
    unittest.main()
