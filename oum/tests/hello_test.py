import time
from selenium.webdriver.common import by
from selenium import webdriver
import unittest

from ..uiapps import uiacontractfortest

class BaseUiTestCase(unittest.TestCase):
    def setUp(self):
        # put it in setUp
        self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                  desired_capabilities={
                                      #'debugConnectToRunningApp': 'true',
                                      'debugConnectToRunningApp': 'false',
                                      'app': uiacontractfortest.OUM_TESTWPFAPP_EXE_PATH,
                                      'args': ''})
        #time.sleep(2)
        pass

    def tearDown(self):
        self.driver.close()
        pass

class BasicSeleniumElementRetrieveAndPropertyAcessTestCase(BaseUiTestCase):
    def test_get_one_by_id(self):
        txt_name_holder_element=self.driver.find_element(by=by.By.ID, value=uiacontractfortest.OUM_TESTWPFAPP_EXE_PATH_AUID_BTN_OPEN_NAME_HOLDER)
        actual_value=txt_name_holder_element.text
        expect_value=uiacontractfortest.OUM_TESTWPFAPP_EXE_ADEFAULTVALUE_BTN_OPEN_NAME_HOLDER
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
