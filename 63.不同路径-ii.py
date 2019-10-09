#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (31.70%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 71.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:return 0
        row_len=len(obstacleGrid)
        col_len=len(obstacleGrid[0])
        obstacleGrid[0][0] =1-obstacleGrid[0][0]
        for r in range(1,row_len):
            obstacleGrid[r][0]=obstacleGrid[r-1][0]*(obstacleGrid[r][0]==0)
        for c in range(1,col_len):
            obstacleGrid[0][c]=obstacleGrid[0][c-1]*(obstacleGrid[0][c]==0)
        for r in range(1,row_len):
            for c in range(1,col_len):
                obstacleGrid[r][c]=(obstacleGrid[r-1][c]+obstacleGrid[r][c-1])*(obstacleGrid[r][c]==0)
        return obstacleGrid[-1][-1]


