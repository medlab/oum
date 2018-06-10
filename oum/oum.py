from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.remote.webdriver import WebDriver, WebElement

class SeleniumElementProxyBase:
    def __init__(self, find_by=by.By.ID, by_value=None, lazy=True, dirty=False):
        # self.driver=driver # type: WebDriver
        # self.parent_selenium_element=parent_selenium_element # type: WebElement
        self.find_by=find_by
        self.by_value=by_value

        self.lazy=lazy
        self.dirty=dirty

        self.driver=None
        self.parent_selenium_element=None
        pass

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, value):
        self._driver=value
        pass

    @property
    def parent_selenium_element(self):
        return self._parent
        return

    @parent_selenium_element.setter
    def parent_selenium_element(self, value):
        self._parent=value
        pass

    pass

class SeleniumElementProxy(SeleniumElementProxyBase):
    def __init__(self, *args, **kwargs):
        super(self).__init__(*args, **kwargs)
        self.real_element=None
        pass

    def __getattr__(self, attr):
        if self.dirty or (self.real_element==None and self.lazy):
            find_root=self.driver if self.parent_selenium_element==None else self.parent_selenium_element
            self.real_element=find_root.find_element(self.find_by, self.by_value)
            self.dirty=False

        return getattr(self.real_element, attr)
    pass

class SeleniumElementsProxy(SeleniumElementProxyBase): # TODO bad design here, just for convenience
    def __init__(self, *args, **kwargs):
        super(self).__init__(*args, **kwargs)
        self.real_element_list=None
        pass

    def get_list(self):
        '''

        :return:
        :rtype: list[WebElement]
        '''
        if self.dirty or (self.real_element_list==None and self.lazy):
            find_root=self.driver if self.parent_selenium_element==None else self.parent_selenium_element
            self.real_element_list=find_root.find_elements(self.find_by, self.by_value)
            self.dirty=False

        return self.real_element_list

    pass

class OUMElement:
    def __init__(self, driver, parent_selenium_element, find_by=by.By.ID, is_list=False, by_value=None, lazy=True, dirty=False):
        self.driver=driver # type: WebDriver
        self.parent_selenium_element=parent_selenium_element # type: WebElement
        self.find_by=find_by
        self.by_value=by_value
        self.is_list=is_list

        self.lazy=lazy
        self.dirty=dirty

        self.value_attr_key=f'{self.find_by}#{self.by_value}'
        pass

    def __set__(self, instance, value):
        raise NotImplementedError("[OUM]assign is not support")
        pass

    def __delete__(self, instance):
        raise NotImplementedError("[OUM]delete is not support")
        pass

    def __get__(self, instance):
        if not hasattr(instance, self.value_attr_key):
            a_proxy_element=SeleniumElementsProxy(self.find_by, self.by_value, self.lazy, self.dirty) if self.is_list else SeleniumElementProxyBase(self.find_by, self.by_value, self.lazy, self.dirty)
            setattr(instance, self.value_attr_key, a_proxy_element)

        return getattr(instance, self.value_attr_key)
        pass

    pass

def auto_set_all_oum_element_driver_attr(target_page_obj, driver): #TODO seems not work!
    '''
    auto fill the driver context to all OUMElement
    :param target_page_obj:
    :param driver:
    :return:
    '''

    import inspect
    target_class=target_page_obj.__class__
    all_oum_pd=[pd for pd in dir(target_class) if isinstance(getattr(target_class, pd), OUMElement)]
    all_oum_pd_obj=[getattr(target_class,pd) for pd in all_oum_pd]
    for pd_obj in all_oum_pd_obj: # type: OUMElement
        selenium_element_proxy=pd_obj.__get__(target_page_obj)  # type: SeleniumElementProxyBase
        selenium_element_proxy.driver=driver
        pass
    pass