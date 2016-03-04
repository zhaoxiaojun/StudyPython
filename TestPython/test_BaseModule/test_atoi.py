#coding=utf8
'''
实现atoi这个函数，将一个字符串转换为整数。如果没有合法的整数，返回0。如果整数超出了32位整数的范围，返回INT_MAX(2147483647)如果是正整数，
或者INT_MIN(-2147483648)如果是负整数。
'''
class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        INT_MAX = pow(2,31)-1
        INT_MIN = pow(2,31)*(-1)
        NumStrL = ['0','1','2','3','4','5','6','7','8','9']
        i = 0
        flag = True

        sstr = str.strip()
        if len(sstr) == 0:
            return 0
        if sstr[0] == '-':
            flag = False
            sstr = sstr[1:]
        elif sstr[0] == '+':
            sstr = sstr[1:]


        while((i<len(sstr)) and (sstr[i] in NumStrL)):
            i = i + 1

        sstr = sstr[:i]
        sstr = sstr.split('.')[0]

        try:
            result = int(sstr)
        except ValueError:
            return 0

        if flag:
            if result > INT_MAX:
                return INT_MAX
            return result
        else:
            result = -1 * result
            if result < INT_MIN:
                return INT_MIN
            return result



SolutionO = Solution()
str1 = '-2023'
print SolutionO.atoi(str1)
