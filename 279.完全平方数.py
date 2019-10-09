#
# @lc app=leetcode.cn id=279 lang=python
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (50.82%)
# Likes:    193
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 40.7K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 示例 1:
# 
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 
# 示例 2:
# 
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# 
#
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        for i in range(1,n+1):
            j=1
            imin=float('inf')
            while i-j*j>=0:
                imin=min(imin,dp[i-j*j]+1)
                j+=1
            dp[i]=imin
        return dp[n]
            



