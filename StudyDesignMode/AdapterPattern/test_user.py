#coding=utf8

"""
#不适用适配器模式
class User(object):
    def create_or_update(self):
        pass

class Profile(object):
    def create_or_update(self):
        pass

user = User()
user.create_or_update()

profile = Profile()
profile.create_or_update()

#如果需要在不同的地方做同样的事，或是在不同的项目中重用这段代码，那么需要重新敲一遍
"""

class User(object):
    def create_or_update(self):
        pass

class Profile(object):
    def create_or_update(self):
        pass

class Account():
    def new_account(self):
        user = User()
        user.create_or_update()
        profile = Profile()
        profile.create_or_update()

account_domain = Account()
account_domain.new_account()

'''
这样的话，你就能够在你需要的时候使用账户domain了，你也可以将其他的类包装到domain类下
'''
