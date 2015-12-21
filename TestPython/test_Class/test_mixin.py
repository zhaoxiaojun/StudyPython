#coding=utf8
class Fruit(object):
       pass

class GiftMixin(object):   #可以作为礼物
       def is_gift_fruit(self):
              return True

class NotGiftMixin(object):   #不可以作为礼物
       def is_gift_fruit(self):
              return False

class PareMixin(object):    #削皮
       def eat_method(self):
              return 'Pare'

class HuskMixin(object):  #剥皮
       def eat_method(self):
              return 'Husk'
class Apple(GiftMixin, PareMixin, Fruit):pass
class Orange(GiftMixin, HuskMixin, Fruit):pass
class Pear(NotGiftMixin, PareMixin, Fruit):pass
class Banana(NotGiftMixin, HuskMixin, Fruit):pass
