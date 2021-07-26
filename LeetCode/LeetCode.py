# coding=utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class solution:

    def decode_at_index(self, s: str, k: int):
        '''
        s=a234567899999999时系统卡死
        Q:
给定一个编码字符串 S。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：

如果所读的字符是字母，则将该字母写在磁带上。
如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。
        '''
        temp = ''
        if not s or k <= 0:
            return False
        for char_in_s in s:
            if char_in_s.isalpha():
                temp += char_in_s
            elif char_in_s.isalnum():
                temp = temp * int(char_in_s)
        print(temp)
        return temp[k - 1]

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Q:给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。
        """
        head = ListNode(None)
        l1_s = ''
        l2_s = ''
        head.next = l1
        while head.next:
            l1_s += str(head.next.val)
            head = head.next
        head = ListNode(None)
        head.next = l2
        while head.next:
            l2_s += str(head.next.val)
            head = head.next
        sum_result = str(int(l1_s[::-1]) + int(l2_s[::-1]))[::-1]
        head = tail = ListNode(sum_result[0])
        for s in sum_result[1:]:
            new_Node = ListNode(int(s))
            tail.next = new_Node
            tail = new_Node
        return head

    def length_of_longest_substring(self, s: str):
        """
        给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
        """
        new_s = ''
        substring_length_list = []
        if s == '':
            return 0
        for i in range(len(s)):
            new_s += s[i]
            for sub_s in s[i + 1:]:
                if sub_s not in new_s:
                    new_s += sub_s
                else:
                    substring_length_list.append(len(new_s))
                    new_s = ''
                    break
            if new_s != '':
                substring_length_list.append(len(new_s))
                new_s = ''
        return max(substring_length_list)

    def find_median_sortedarrays(self, nums1: list, nums2: list) -> float:
        '''
        给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
        '''
        new_list = sorted(nums1 + nums2, reverse=False)
        length = len(new_list)
        if length % 2 == 1:
            return float(new_list[int(length / 2)])
        else:
            return (new_list[int(length / 2)] + new_list[int(length / 2) - 1]) / 2.0

    def longets_palindrome(self, s: str) -> str:
        '''
        给你一个字符串 s，找到 s 中最长的回文子串。
        '''
        result_s = {}
        if s == '' or not s:
            return ''
        for low in range(len(s)):
            hight = len(s) - 1
            while low != hight:
                if s[low] == s[hight]:
                    new_s = s[low:hight + 1]
                    if new_s == new_s[::-1]:
                        result_s[len(new_s)] = new_s
                        low = hight
                        hight = len(s) - 1
                        break
                hight -= 1
        if not result_s:
            return s[0]
        return result_s[max(result_s.keys())]

    def convert(self, s: str, num_rows: int) -> str:
        '''
        将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。
        比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：
        P   A   H   N
        A P L S I I G
        Y   I   R
        之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
        '''
        new_s_list = [[] for i in range(num_rows)]
        line_num = 0
        direction = True
        result_s = ''
        if num_rows == 1:
            return s
        for char_s in s:
            if direction:
                new_s_list[line_num].append(char_s)
                line_num += 1
            if line_num == num_rows:
                line_num -= 2
                direction = False
                continue
            if not direction:
                new_s_list[line_num].append(char_s)
                line_num -= 1
            if line_num <= 0:
                direction = True
        print(new_s_list)
        for new_s in new_s_list:
            result_s += ''.join(new_s)
        return result_s

    def reverse_int(self, x: int) -> int:
        '''
        给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−2^31, 2^31− 1] ，就返回 0。
        '''
        nums = str(x)[::-1]
        if int(nums) > 2 ** 31 - 1:
            return 0
        elif x > 0:
            return int(nums)
        else:
            return int('-' + nums)

    def my_a_to_i(self, s: str) -> int:
        """
        请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
        """
        is_negative = False
        new_s = ''
        s = s.lstrip().rstrip()
        if s == '':
            return 0
        if s[0] == '-':
            s = s[1:]
            is_negative = True
        elif s[0] == '+':
            s = s[1:]
        for char_s in s:
            if char_s >= '0' and char_s <= '9':
                new_s += char_s
            else:
                break
        if new_s == '':
            return 0
        ouput_number = int(new_s)
        if is_negative:
            ouput_number = -1 * ouput_number
        if ouput_number > 2 ** 31 - 1:
            ouput_number = 2 ** 31 - 1
        elif ouput_number < -2 ** 31:
            ouput_number = -2 ** 31
        return ouput_number

    def is_palindrome(self, x: int) -> bool:
        """
        给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是
        """
        s = str(x)
        hight = len(s) - 1
        low = 0
        while hight - low >= 0:
            if s[hight] != s[low]:
                return False
            else:
                low += 1
                hight -= 1
        return True
        # if s == s[::-1]:
        #     return True
        # else:
        #     return False

    def is_match(self, s: str, p: str) -> bool:
        """
        给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。
        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素
        所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
        """
        import re
        if not re.fullmatch(p, s):
            return False
        return True

    def max_area(self, height: list) -> int:
        """
        给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点(i,ai) 。在坐标内画 n 条垂直线，垂直线 i的两个端点分别为(i,ai) 和 (i, 0) 。
        找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。
        """
        n = len(height)
        if n <= 1:
            return 0
        elif n == 2:
            return min(height)
        low = 0
        hight = n - 1
        temp_area = 0
        while low < hight:
            temp_area = max(temp_area,
                            (hight - low) * min(height[hight], height[low]))
            if height[hight] >= height[low]:
                low += 1
            else:
                hight = hight - 1
        return temp_area

    def int_to_roman(self, num:int)->str:
        """
        罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
        字符          数值
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
        通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
        数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
        同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
        I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
        X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
        C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
        给你一个整数，将其转为罗马数字。
        """
        roman_num = {0: '',1:'I',2:'II',3:'III', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        s = ''
        i = len(str(num))
        if num > 3999 or num < 0:
            return s
        while i>0:
            a,b  = divmod(num,10 ** (i-1))
            c = a
            key = a * 10 ** (i-1)
            if key in roman_num.keys():
                s += roman_num[key]
            else:
                while key > 5 * 10 ** (i-1):
                    s += roman_num[5 * 10 ** (i-1)]
                    # key = key - 5 * 10 ** i
                    c = c - 5
                    key = key - 5 * 10 ** (i-1)
                else:
                    s += roman_num[int(key / c)] * int(key / 10 ** abs(i-1))
            num = num - a * 10 ** (i-1)
            i = i - 1
        return s
            
    def roman_to_int(self, s: str)->int:
        """罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。"""
        roman_num = {'': 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 
                     'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD':400,'CM': 900}
        num = 0
        i = 0
        while i<len(s):
            if i+1>=len(s):
                temp = '' 
            else:
                temp = s[i+1]
            if s[i]+temp in roman_num.keys():
                num += roman_num[s[i]+temp]
                i += 2
            else:
                num += roman_num[s[i]]
                i += 1
        return num
    
    
    def longest_common_prefix(self,strs)->str:
        """
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
        """
        short_s=min(strs)
        def is_startwith(s:str,p:str):
            if not s.startswith(p):
                return False
            return True
        while short_s:
            is_check = []
            for char_s in strs:
                check = is_startwith(char_s,short_s)
                if not check:
                    short_s = short_s[:-1]
                else:
                    is_check.append(1)
            if len(is_check) == len(strs):
                return short_s
        return ''
    
    def three_sum(self, nums:list)->list:
        """
        给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
        注意：答案中不可以包含重复的三元组。
        """
        n = len(nums)
        if n < 3 :
            return []
        sum_list = []
        nums = sorted(nums)
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            for second in range(first+1,n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[third] + nums[second] > -nums[first]:
                    third -= 1
                if second == third:
                    break
                if nums[third] + nums[second] == -nums[first]:
                    sum_list.append([nums[first],nums[second],nums[second]])
        return sum_list
                
    def three_sum_closest(self, nums: list,target: int)->int:
        """
        给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
        返回这三个数的和。假定每组输入只存在唯一答案。
        """
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        sum_result = 0
        temp = 10 ** 4
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            second = first + 1
            while second < third:
                temp_target = nums[first] + nums[second] + nums[third]
                if temp_target == target:
                    return temp_target
                if abs(temp_target - target) < abs(temp - target):
                    temp = temp_target
                if temp_target > target:
                    temp_third = third - 1
                    while second < temp_third and nums[third] == nums[temp_third]:
                        temp_third -= 1
                    third = temp_third
                else:
                    temp_second = second + 1
                    while temp_second < third and nums[second] == nums[temp_second]:
                        temp_second += 1
                    second = temp_second
        return temp
    
    def letter_combinations(self, digits:str)->list:
        """
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射-手机上的九键键盘（与电话按键相同）。注意 1 不对应任何字母。
        """
        letter_list = []
        letter_init_dict = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        print(letter_init_dict)
        init_s = list(digits)
        for i in range(len(init_s)):
            init_s[i] = list(letter_init_dict[init_s[i]])
        temp = []
        for letter_l in init_s:
            if not letter_list:
                letter_list = letter_l
                continue
            for s in letter_list:
                for char_s in letter_l:
                    temp.append(s+char_s)
            letter_list = temp
            temp = []
        return letter_list
    
    def four_sum(self, nums: list,target: int)-> list:
        """
        给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
        使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
        注意：答案中不可以包含重复的四元组。
        """
        n = len(nums)
        nums.sort()
        sum_list = []
        temp = 10 ** 4
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first+1,n):
                if second > first+1 and nums[second] == nums[second - 1]:
                    continue
                third = second + 1
                four = n - 1
                while third < four:
                    temp_target = nums[first] + nums[second] + nums[third] + nums[four]
                    if temp_target == target:
                        x = [nums[first], nums[second], nums[third], nums[four]]
                        if x not in sum_list:
                            sum_list.append(x)
                    if temp_target > target:
                        temp_four = four - 1
                        while four < temp_four and nums[four] == nums[temp_four]:
                            temp_four -= 1
                        four = temp_four
                    else:
                        temp_third = third + 1
                        while temp_third < third and nums[third] == nums[temp_third]:
                            temp_third += 1
                        third = temp_third
        return sum_list
    
    def remove_nth_from_end(self,head,n:int):
        """
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
head:ListNode
        """
        node_count = 0
        h_1=h_2=h_3=tail = head
        while tail:
            node_count += 1
            tail = tail.next
            if node_count <= n:
                continue
            h_2 = h_2.next
            if node_count - n > 1:
                h_1 = h_1.next
        if node_count == n:
            h_3 = h_3.next
        else:
            h_1.next = h_2.next
        return h_3
        # while node_head:
        #     node_count += 1
        #     node_head = node_head.next
        # remove_index = node_count - n 
        # n_h = tail = head
        # num = 0
        # while tail:
        #     if remove_index == 0:
        #         n_h = n_h.next
        #         break
        #     num += 1
        #     if num == remove_index:
        #         tail.next = tail.next.next
        #         break
        #     tail = tail.next
        # return n_h 
        
    def is_valid(self, s:str)->bool:
        """
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
        有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合
        """
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''
    
    def merge_two_lists(self, l1, l2):
        """
        将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
        """
        head_l1 = per_l1 = ListNode(None)
        head_l1.next = per_l1.next = l1
        tail_l1 = l1
        head_l2 = current_l2 = l2
        list_count = 0
        while tail_l1 and head_l2:
            list_count += 1
            if tail_l1.val < current_l2.val:
                tail_l1 = tail_l1.next
                if per_l1.next.next == tail_l1:
                    per_l1 = per_l1.next
                continue
            else:
                head_l2 = head_l2.next
                current_l2.next = per_l1.next
                per_l1.next = current_l2
                current_l2 = head_l2
                per_l1 = per_l1.next
        if not tail_l1 and head_l2:
            if list_count == 0:
                return head_l2
            per_l1.next = head_l2
        return head_l1.next
        # new_list_node = tail = ListNode(None)
        # head_l1 = l1
        # head_l2 = l2
        # while head_l2 and head_l1:
        #     if head_l1.val > head_l2.val:
        #         new_list_node.next = head_l2
        #         head_l2 = head_l2.next
        #     elif head_l1.val < head_l2.val:
        #         new_list_node.next = head_l1
        #         head_l1 = head_l1.next
        #     else:
        #         new_list_node.next = head_l2
        #         head_l2 = head_l2.next
        #         new_list_node = new_list_node.next
        #         new_list_node.next = head_l1
        #         head_l1 = head_l1.next
        #     new_list_node = new_list_node.next
        # if not head_l1 and head_l2:
        #     new_list_node.next = head_l2
        # elif not head_l2 and head_l1:
        #     new_list_node.next = head_l1
        # tail = tail.next
        # return tail
        
    def merge_k_lists(self, lists: list):
        """
        给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
        """
        if not lists:
            return None
        temp_list = None
        for i in range(len(lists)):
            temp_list = self.merge_two_lists(lists[i], temp_list)
        return temp_list
    
    def generate_parenthesis(self, n: int)->list:
        """
        数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
        """
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            for left in self.generate_parenthesis(c):
                for right in self.generate_parenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
        
        
    def swap_pairs(self, head):
        """
        给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
        """
        head_node = p_per_node = ListNode(None)
        head_node.next = head
        p_per_node.next = head
        per_node = head
        if not head:
            return None
        tail = per_node.next
        while tail:
            per_node.next = tail.next
            tail.next = per_node
            p_per_node.next = tail
            p_per_node = per_node
            per_node = per_node.next
            if not per_node:
                break
            tail = per_node.next
        return head_node.next
        
    def reverse_k_group(self, head, k: int):
        """
        给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
        """
        
        def reverse(self, head: ListNode, tail: ListNode):
            prev = tail.next
            p = head
            while prev != tail:
                nex = p.next
                p.next = prev
                prev = p
                p = nex
            return tail, head
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return hair.next
    
    def divide(self, dividend: int, divisor: int)->int:
        """
        给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
        """
        temp_quotient = 7
        dividend_str = str(dividend)
        dividend_len = len(dividend_str)
        temp_dividend = 0
        quotient = 0
        is_negative = False
        temp_dividend_1 = -1
        if str(divisor)[0] == '-':
            divisor = int(str(divisor)[1:])
            is_negative = True
        for i in range(dividend_len):
            if dividend_str[i] == '-':
                if is_negative:
                    is_negative = False
                else:
                    is_negative = True
                continue
            temp_dividend += int(dividend_str[i])
            if temp_dividend < divisor:
                temp_dividend = temp_dividend * 10
                continue
            # temp_dividend_1 = temp_dividend - temp_quotient * divisor
            while temp_dividend_1 < 0:
                temp_quotient -= 1
                temp_dividend_1 = temp_dividend - temp_quotient * divisor
            while temp_dividend_1 >= divisor:
                temp_quotient += 1
                temp_dividend_1 = temp_dividend - temp_quotient * divisor
            temp_dividend = temp_dividend_1 * 10
            quotient += temp_quotient * 10 ** (dividend_len - i - 1)
            temp_quotient = 7
            temp_dividend_1 = -1
        if is_negative:
            quotient = -1 * int(quotient)
        if quotient > 2 ** 31 -1 :
            quotient = 2 ** 31 - 1
        elif quotient < -2 ** 31:
            quotient = -2 ** 31
        return quotient
            
    def next_permutation(self, nums: list):
        """
        搞不懂
        实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
        如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
        必须 原地 修改，只允许使用额外常数空间。
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
    def remove_duplicates(self, nums: list)->int:
        """
        给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
        """
        temp = 0
        n = len(nums)
        first = second = 1
        while first < n:
            if nums[first] != nums[first - 1]:
                nums[second] = nums[first]
                second += 1
            first += 1
        nums = nums[:second]
        return len(nums)
        # i = 0
        # while i < n - 1:
        #     if nums[i] == nums[i + 1]:
        #         nums.remove(nums[i])
        #         n = len(nums)
        #         i -= 1
        #     i += 1
        # return nums
            
    def remove_element(self, nums: list, val: int)->int:
        """
        给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
        不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
        元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
        """
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums.remove(nums[i])
                n = len(nums)
                i -=1
            i += 1
        return nums
    
    def str_str(self, haystack: str, needle: str)->int:
        """
        给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
        如果不存在，则返回  -1 。
        """
        if needle == '' or not needle:
            return 0
        for i in range(len(haystack)):
            if i + len(needle) > len(haystack):
                return -1
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        # try:
        #     return haystack.index(needle)
        # except Exception as e:
        #     return -1
        
    
    def find_sub_string(self, s: str, words: list)->list:
        """
        给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序
1、计算words中每个单词出现的次数，即一张哈希表
2、采用滑动窗口的方法，一次获取s中长度为len(words) * len(words[0])的单词
3、在2获取的单词中，每经过len(words[0])记为一个单词添加到临时列表中，然后计算临时表中欧给你每个单词出现的次数，即一张哈希表
4、比较1和3两张哈希表，如果相同则表示通过，
        """
        from collections import Counter
        sub_string_index_list = []
        s_index = 0
        word_index = 0
        len_s = len(s)
        len_words = len(words)
        len_word = len(words[0])
        words = Counter(words)
        for i in range(len_s):
            temp_s = s[i:i+len_words * len_word]
            j = 0
            temp_list = []
            while j <= len(temp_s) - len_word:
                temp_list.append(temp_s[j:j+len_word])
                j += len_word
            if words == Counter(temp_list):
                sub_string_index_list.append(i)
        return sub_string_index_list
    
    def search_insert(self, nums: list, target: int)->int:
        """
        给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，
        返回它将会被按顺序插入的位置。
        你可以假设数组中无重复元素。
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == target or nums[i] > target:
                return i
        return n
    
    def search_range(self, nums: list, target: int)->list:
        """
        给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
        """
        try:
            left =  nums.index(target)
            temp_l = left
            right = len(nums) - 1
            while temp_l <= right:
                if nums[temp_l] == target:
                    temp_l += 1
                else:
                    right = temp - 1
                    break
                # mid = int((temp_l + right) / 2)
                # if nums[mid] == target:
                #     temp_l = mid + 1
                # else:
                #     right = mid - 1
            return [left, right]
        except:
            return [-1,-1]
        # n = len(nums)
        # local_list = []
        # for i in range(n):
        #     if nums[i] == target:
        #         local_list.append(i)
        #     if nums[i] > target:
        #         break
        # if not local_list:
        #     local_list = [-1,-1]
        # return [local_list[0], local_list[len(local_list) - 1]]
        
    
    def search(self, nums: list, target: int)->int:
        """
        整数数组 nums 按升序排列，数组中的值 互不相同 。
        在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
        使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
        例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
        给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
        """
        try:
            return nums.index(target)
        except:
            return -1
        
    def is_valid_sudoku(self, board: list)->bool:
        """
        请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
        数独部分空格内已填入了数字，空白格用 '.' 表示。
        注意：
        一个有效的数独（部分已被填充）不一定是可解的。
        只需要根据以上规则，验证已经填入的数字是否有效即可
        """
        def check_number_count(nums):
            from collections import Counter
            num_count_dict = Counter(nums)
            for key,value in num_count_dict.items():
                if key == '.':
                    continue
                else:
                    if value > 1:
                        return False
            return True
        import numpy as np
        np_board = np.array(board)
        np_board_T = np_board.T
        row_valid = True
        col_valid = True
        row_index = 0
        col_index = 0
        temp_valid = True
        i = 0
        while row_index < np_board.shape[0]:
            row_valid = row_valid and check_number_count(np_board[i])
            col_valid = col_valid and check_number_count(np_board_T[i])
            # print(np_board[row_index:row_index+3,col_index:col_index + 3])
            temp_valid = temp_valid and check_number_count(list(np_board[row_index:row_index+3,col_index:col_index + 3].flatten()))
            if col_index < 6:
                col_index += 3
            else:
                row_index += 3
                col_index = 0
            i += 1
        return row_valid and col_valid and temp_valid
    
    def solve_sudoku(self, board:list)->None:
        """
        抄袭题解
        编写一个程序，通过填充空格来解决数独问题。
        数独的解法需 遵循如下规则：
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
        数独部分空格内已填入了数字，空白格用 '.' 表示。
        """
        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            
            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] == False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return
            
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True

        dfs(0)
        
    def count_and_say(self, n: int)->str:
        '''
        给定一个正整数 n ，输出外观数列的第 n 项。「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：
countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
        '''
        def get_s(temp):
            s = ''
            t = ''
            count = 1
            for i in range(len(temp)):
                if t == temp[i]:
                    count += 1
                else:
                    if t != '':
                        s += str(count) + t
                        count = 1
                    t = temp[i]
            s += str(count) + t
            return s
        num = 2
        temp = '1'
        s = '11'
        if n == 1:
            s = '1'
        while num < n:
            s = get_s(s)
            num += 1
        return s
                
                
    def combination_sum(self, candidates: list, target: int)->list:
        '''
        给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，
        找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
        '''
        result = []
        def combination_s(candidates, target, combine):
            if target < 0:
                return
            if target == 0:
                result.append(combine)
            for i,c in enumerate(candidates):
                combination_s(candidates[i:], target - c, combine + [c])
        combination_s(candidates, target, [])
        return result
        
    def first_missing_positive(self, nums: list)->int:
        """
        给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
        """
        nums.sort()
        left_index = 0
        try:
            while left_index < len(nums):
                if nums[left_index] < 0:
                    nums.remove(nums[left_index])
                else:
                    if nums[0] - 1 > 0 :
                        return 1
                    if nums[left_index] == nums[left_index + 1] or nums[left_index] + 1 == nums[left_index + 1]:
                        left_index += 1
                    elif nums[left_index] + 1 != nums[left_index + 1]:
                        return nums[left_index] + 1
            if not nums:
                return 1
        except:
            print(nums)
            return nums[-1] + 1
            
    def trap(self, height: list)->int:
        """
        给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
        """
        trap_area = 0
        def get_aera(h:list, weight: int, min_h: int, a:int):
            left_index = 0
            temp =  (min_h - a) * weight
            while left_index < len(h):
                if h[left_index] > a :
                    if h[left_index] <= min_h:
                        temp = temp - h[left_index] + a
                    else:
                        temp = temp - min_h + a
                left_index += 1
            return temp
        def init_height(h:list):
            left_index = 0
            right_index = len(h) - 1
            try:
                while h:
                    if h[left_index] < h[left_index + 1]:
                        h.remove(h[left_index])
                    else:
                        break
                right_index = len(h) - 1
                while right_index >= 1:
                    if h[right_index] <= h[right_index - 1]:
                        h = h[:right_index]
                        right_index -= 1
                    else:
                        break
            finally:
                return h
        def area(height, a):
            nonlocal trap_area
            height = init_height(height)
            # print(height)
            if len(height) <= 1:
                return 
            left_index = 0
            right_index = len(height) - 1
            min_h = min(height[left_index], height[right_index])
            trap_area += get_aera(height, right_index + 1, min_h, a)
            print(trap_area)
            
            area(height, min_h)
        area(height, 0)
        return trap_area
    
    def restore_arry(self):
        """
        """
            
    
# head = tail = ListNode(None)
# for i in range(1,7):
#     tail.next = ListNode(i)
#     tail = tail.next
# head = head.next
solute = solution()
print(solute.trap(height =[8,2,8,9,0,1,7,7,9]))