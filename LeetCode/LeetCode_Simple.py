#coding=utf-8
class leetcode_simple:

    def length_of_last_word(self, s: str)->int:
        """
        58:给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
        单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
        """
        s = s.rstrip().split(' ')
        return len(s[-1])

    def plus_one(self, digits: list)->list:
        """
        66 加一:给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。需要注意为9的情况
for i in range (len(digits)-1,-1,-1):
            if digits [i] != 9:
                digits [i] = digits [i] + 1
                return digits
            else:
                digits [i] = 0
        digits.append(1)
        digits.reverse()
        return digits
        """
        n = len(digits)
        idx = n - 1
        plus = 1
        while idx >= 0:
            temp = digits[idx] + plus
            if temp > 9:
                plus = 1
                digits[idx] = temp - 10
            else:
                plus = 0
                digits[idx] = temp
                break
            idx -= 1
        if plus == 1:
            digits = [plus] + digits
        return digits
        
    def add_binary(self, a: str, b: str)->str:
        """
        67:二进制求和：给你两个二进制字符串，返回它们的和（用二进制表示）。
                      输入为 非空 字符串且只包含数字 1 和 0。
        """
        """#方法一：
        a = '0b' + a
        b = '0b' + b
        return eval('bin({0} + {1})'.format(a,b)).replace('0b','')"""
        n = len(a)
        m = len(b)
        ans = ''
        plus = '0'
        if n > m:
            b = '0' * (n - m) + b
        else:
            a = '0' * (m - n) + a
        for i in range(len(a)-1, -1, -1):
            if a[i] == b[i] == '1':
                if plus == '1':
                    ans += '1'
                else:
                    ans += '0'
                    plus = '1'
            else:
                t = max(a[i],b[i])
                if t == plus == '1':
                    ans += '0'
                elif t == plus == '0':
                    ans += '0'
                else:
                    ans += '1'
                    plus = '0'
        if plus == '1':
            ans += plus
        return ans[::-1]

ls = leetcode_simple()
print(ls.add_binary('11','1'))