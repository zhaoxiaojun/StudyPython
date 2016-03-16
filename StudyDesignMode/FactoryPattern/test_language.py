#coding=utf8

class ChaneseGetter(object):
    def __init__(self):
        self.trans = dict(dog="犬", cat="猫", parrot= "鹦鹉")

    def get(self, msgid):
        try:
            return unicode(self.trans[msgid], "utf-8")
        except KeyError:
            return unicode(msgid)

class EnglishGetter(object):
    def get(self, msgid):
        return unicode(msgid)


def get_localizer(language="English"):
    languages = {"English": EnglishGetter, "Chanese": ChaneseGetter}
    return languages[language]()

e = get_localizer("English")
c = get_localizer("Chanese")


for msgid in "dog parrot cat".split():
    print e.get(msgid), c.get(msgid)
