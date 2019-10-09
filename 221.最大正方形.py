#
# @lc app=leetcode.cn id=221 lang=python
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (38.20%)
# Likes:    139
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 31.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:return 0
        res=0
        row=len(matrix)
        col=len(matrix[0])
        dp=[[0 for _ in range(col+1)] for _ in range(row+1)]
        
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j]=min(int(dp[i-1][j-1]),int(dp[i-1][j]),int(dp[i][j-1]))+1
                    res=max(res,dp[i][j])
        return res*res


