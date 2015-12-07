#coding=utf8

def diy_assert(self, a, b):
	self.assertEqual(a, b, 'test fail!')
	self.assertGreater(a, 1000, 'test fail!')