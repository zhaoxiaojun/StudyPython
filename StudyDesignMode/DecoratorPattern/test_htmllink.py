#coding=utf8

class HtmlLinks():
    def set_html(self, html):
        self.html = html

    def get_html(self):
        return self.html

    def render(self):
        print(self.html)

class LogoutLink(HtmlLinks):
    def __init__(self):
        self.html = "<a href="logout.html"> Logout </a>"

class LogoutLinkH2Decorator(HtmlLinks):
    def __init__(self, logout_link):
        self.logout_link = logout_link
        self.set_html(" {0} ".format(self.logout_link.get_html()))

    def call(self, name, args):
        self.logout_link.name(args[0])

class LogoutLinkUnderlineDecorator(HtmlLinks):
    def __init__(self, logout_link):
        self.logout_link = logout_link
        self.set_html(" {0} ".format(self.logout_link.get_html()))

    def call(self, name, args):
        self.logout_link.name(args[0])

class LogoutLinkStrongDecorator(HtmlLinks):
    def __init__(self, logout_link):
        self.logout_link = logout_link
        self.set_html("<strong> {0} </strong>".format(self.logout_link.get_html()))

    def call(self, name, args):
        self.logout_link.name(args[0])

logout_link = LogoutLink()
is_logged_in = 0
in_home_page = 0

if is_logged_in:
    logout_link = LogoutLinkStrongDecorator(logout_link)
if in_home_page:
    logout_link = LogoutLinkH2Decorator(logout_link)
else:
    logout_link = LogoutLinkUnderlineDecorator(logout_link)

logout_link.render()
