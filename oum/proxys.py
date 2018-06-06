from sqlalchemy import Column, Integer


class BaseUIElementProxy:
    def __init__(self):
        self.selenium_element=None
        self.data_model=None
        self.dirty=True
        pass
    pass

class LabelUIElementProxy(BaseUIElementProxy):
    pass

class ButtonUIElementProxy(BaseUIElementProxy):
    pass


# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
# from sqlalchemy import Column, Integer, String
# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     password = Column(String)
#
#     def __repr__(self):
#        return "<User(name='%s', fullname='%s', password='%s')>" % (
#                             self.name, self.fullname, self.password)
#
# if __name__ == '__main__':
#     a=User()
#     print("hello")

