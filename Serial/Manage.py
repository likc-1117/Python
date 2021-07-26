# coding:utf-8
import re
import sys


def tow_sum(nums: list, target: int):
    index_list = []
    for num in nums:
        div_num = target - num
        if div_num == num and nums.count(num) < 2:
            continue
        if div_num in nums:
            '''
            获取列表中的值以及对应的索引
            '''
            for i, x in enumerate(nums):
                if x == div_num or x == num:
                    if i in index_list:
                        index_list.clear()
                    index_list.append(i)
    return index_list


def max_sum(nums: list, first_length: int, second_length: int):
    sum_result = 0
    result = 0
    result_se = 0
    if first_length + second_length > len(nums) or first_length <= 0 or second_length <= 0:
        return 0
    for start_index in range(len(nums)):
        if first_length + start_index > len(nums):
            break
        for i in range(start_index, first_length + start_index):
            result += nums[i]
        if len(nums) - start_index - 1 >= second_length:
            for sencond_index in range(start_index + first_length, len(nums)):
                if second_length + sencond_index <= len(nums):
                    for j in range(sencond_index, second_length + sencond_index):
                        result_se += nums[j]
                if result + result_se > sum_result:
                    sum_result = result + result_se
                result_se = 0
        else:
            for se_index in range(start_index):
                for j in range(se_index, se_index + second_length):
                    result_se += nums[j]
                if result + result_se > sum_result:
                    sum_result = result + result_se
                result_se = 0
        result = 0
    return sum_result


def maximum(nums: list):
    nums_result = sorted(nums)
    div_result = 0
    result = 0
    if len(nums_result) < 2:
        return 0
    for i in range(len(nums_result) - 1):
        div_result = abs(nums_result[i] - nums_result[i + 1])
        if result < div_result:
            result = div_result
    return result


# print(maximum([3,6,9,1]))

'''
给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。

表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
'''


def calculate(s: str):
    # return eval(s.replace('/', '//'))
    exp_expr = r'\d+'
    num_expr = r'[\+\-/\*]'
    num = re.findall(exp_expr, s)  # 从字符串中将数字取出来
    exp = re.findall(num_expr, s)  # 从字符串中的运算符取出来
    exp_len = len(exp)  # 获取运算符列表的长度
    exp_index = 0
    while exp_index < exp_len:  # 根据题目，由于运算符恒定比数字所在的列表长度少一位，所以使用运算符列表长度作为循环依据
        if exp[exp_index] == '+' or exp[exp_index] == '-':  # 判断获取的运算符类型，判断当前的运算符是否为+或者-
            if '*' in exp or '/' in exp:  # 如果当前还有*或者/在运算符列表中，则直接再次循环
                exp_index += 1
                continue
            elif exp[exp_index] == '+':  # 如果运算符列表中已经没有了*或者/，则按照从左到右运算
                num[exp_index] = int(num[exp_index] + num[exp_index + 1])  # 将运算结果赋值给数据列表中进行替换
                exp.remove('+')  # 运算完成后从运算符列表中去除此运算符
            elif exp[exp_index] == '-':
                num[exp_index] = int(num[exp_index] - num[exp_index + 1])
                exp.remove('-')
        elif exp[exp_index] == '*':
            num[exp_index] = int(num[exp_index] * num[exp_index + 1])
            exp.remove('*')
        elif exp[exp_index] == '/':
            num[exp_index] = int(num[exp_index] // num[exp_index + 1])
            exp.remove('/')
        if exp:  # 如果运算符列表中还有运算符，即运算还没完成
            num.remove(num[exp_index + 1])  # 由于时二元运算，那么运算结束后运算符左侧的数字被新的运算结果替换，运算符右侧的数字则去掉
            exp_len = len(exp)  # 重新获取运算符长度
            exp_index = 0  # 设置从头开始重新检索运算符
        else:
            break
    return num[0]


# print(calculate('14/3*2+2'))
# 先乘除后加减
def calc(s: str):
    result = []
    exp_expr = r'\d+'
    num_expr = r'[\+\-/\*]'
    num = re.findall(exp_expr, s)  # 从字符串中将数字取出来
    exp = re.findall(num_expr, s)  # 从字符串中的运算符取出来
    result.append(int(num[0]))
    for exp_index in range(len(exp)):
        if exp[exp_index] == '/':
            if result[-1] < 0:
                result[-1] = abs(result[-1]) // int(num[exp_index + 1]) * (-1)
            else:
                result[-1] = result[-1] // int(num[exp_index + 1])
        elif exp[exp_index] == '*':
            result[-1] = result[-1] * int(num[exp_index + 1])
        elif exp[exp_index] == '-':
            result.append((-1) * int(num[exp_index + 1]))
        else:
            result.append(int(num[exp_index + 1]))
    return sum(result)


# print(calc('1+14/3*2'))

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''


def tow_sum_target(nums: list, target: int):
    # result = []
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             result.append(i)
    #             result.append(j)
    # return result
    temp = nums.copy()
    temp.sort()
    left_index = 0
    right_index = len(temp) - 1
    while left_index < right_index:
        if temp[left_index] + temp[right_index] > target:
            right_index = right_index - 1
        elif temp[left_index] + temp[right_index] < target:
            left_index += 1
        else:
            break
    p = nums.index(temp[left_index])
    nums.pop(p)
    k = nums.index(temp[right_index])
    if k >= p:
        k += 1
    return [p, k]


# print(tow_sum_target([2, 7, 11, 15], 13))

'''
数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。
'''

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
'''


def reverse(x: int):
    result = 0
    is_negative = False
    if x < 0:
        is_negative = True
        x = -1 * x
    # 方法一
    # x = list(map(int, str(x)))
    # for i in range(len(x) // 2):
    #     temp = x[i]
    #     x[i] = x[len(x) - i - 1]
    #     x[len(x) - i - 1] = temp
    # for i in range(len(x)):
    #     result += x[i] * pow(10, len(x) - i - 1)
    # 方法二：
    x = str(x)
    # num_len = len(str(x))
    # start_index = num_len - 1
    # while start_index >= 0:
    #     result += int(x[start_index]) * pow(10, start_index)
    #     start_index -= 1
    # 方法三:效果最好
    result = int(x[::-1])
    if is_negative:
        result = -1 * result
    if result < pow(-2, 31) or result > (pow(2, 31) - 1):  # 32位有符号整型的数值大小有范围
        return 0
    return result


# print(reverse(-123))
'''
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
0 1 1 2 4 7 13 24 44 
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
'''


def tribonacci(n: int):
    result = 0
    if n < 0 or n > 37:
        return 0
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        result = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
    if result > sys.maxsize:
        return 0
    return result


# print(tribonacci(25))


