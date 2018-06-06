
# class OUMElementAttribute:
#     def __init__(self):
#         pass
#     def __set__(self, instance, value):
#         self.impl.set(instance_state(instance),
#                       instance_dict(instance), value, None)
#
#     def __delete__(self, instance):
#         self.impl.delete(instance_state(instance), instance_dict(instance))
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#
#         dict_ = instance_dict(instance)
#         if self._supports_population and self.key in dict_:
#             return dict_[self.key]
#         else:
#             return self.impl.get(instance_state(instance), dict_)
from selenium import webdriver


class OUMBaseElementAttribute:
    def __init__(self):
        pass

    def __set__(self, instance, value):
        # self.impl.set(instance_state(instance),
        #         #               instance_dict(instance), value, None)
        pass

    def __delete__(self, instance):
        # self.impl.delete(instance_state(instance), instance_dict(instance))
        pass

    def __get__(self, instance, owner):
        # if instance is None:
        #     return self
        #
        # dict_ = instance_dict(instance)
        # if self._supports_population and self.key in dict_:
        #     return dict_[self.key]
        # else:
        #     return self.impl.get(instance_state(instance), dict_)
        pass

    pass


class PageNotepad:
    pass

if __name__ == '__main__':
    a=PageNotepad()

    # put it in setUp
    driver = webdriver.Remote(command_executor='http://localhost:9999',
                                   desired_capabilities={
                                       'debugConnectToRunningApp':'true',
                                       'app': r'C:\Windows\notepad.exe',
                                       'args': ''})
    # put it in test method body
    win = driver.find_element_by_id('WpfTestApplicationMainWindow')
    win.find_element_by_id('SetTextButton').click()
    assert 'CARAMBA' == driver.find_element_by_id('MyTextBox').text

    driver.close()


