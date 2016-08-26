#coding=utf8

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        from functools import cmp_to_key
        key = cmp_to_key(lambda x,y: int(y) - int(x))
        res = ', '.join(sorted(map(str, nums), key=key))
        return res or '0'

nums = [-1,-2,3,4,9,2,3,4,5]
print nums
s = Solution()
print map(str, nums)
print s.largestNumber(nums)

print
nums = {1,010,3,4,9,2,3,4,5}
print nums
print map(str, nums)
print s.largestNumber(nums)


"""
将老式的比较函数（comparison function）转化为关键字函数（key function）。
该函数主要用来将程序转成Python 3格式的，因为Python 3中不支持比较函数。比较函数是可调用的，接受两个参数，比较这两个参数并根据他们的大小关系返回负值、
零或正值中的某一个。关键字函数也是可调用的，接受一个参数，同时返回一个可以用作排序关键字的值。
"""
