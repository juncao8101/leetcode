#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (47.25%)
# Likes:    147
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 20.9K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly=[1]
        i2,i3,i5=0,0,0
        while n>=2:
            next2,next3,next5=ugly[i2]*2,ugly[i3]*3,ugly[i5]*5
            next=min(next2,next3,next5)
            if next==next2:
                i2+=1
            if next==next3:
                i3+=1
            if next==next5:
                i5+=1
            ugly.append(next)
            n-=1
        print(ugly)
        return ugly[-1]
        

