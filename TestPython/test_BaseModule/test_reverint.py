#coding=utf8

#反转整数
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        flag = True
        if n < 0:
            flag = False
            n = -1 * n

        strn = str(n)
        strn = strn[::-1]
        try:
            if flag:
                return int(strn)
            else:
                return int(strn) * (-1)
        except:
            return 0

SolutionO = Solution()
n = 1534236469
print SolutionO.reverseInteger(n)
