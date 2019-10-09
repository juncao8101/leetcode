#
# @lc app=leetcode.cn id=64 lang=python
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (62.26%)
# Likes:    281
# Dislikes: 0
# Total Accepted:    32K
# Total Submissions: 51.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        column=len(grid[0])
        for i in range(1,column):
            grid[0][i]+=grid[0][i-1]
        for j in range(1,row):
            grid[j][0]+=grid[j-1][0]
        
        for j in range(1,row):
            for i in range(1,column):
                grid[j][i]+=min(grid[j][i-1],grid[j-1][i])
        return grid[-1][-1]



