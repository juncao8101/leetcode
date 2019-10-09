#
# @lc app=leetcode.cn id=304 lang=python
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (40.51%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 7.9K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
# 
# 
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
# 
# 示例:
# 
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 说明:
# 
# 
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2。
# 
# 
#

# @lc code=start
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return 
        m=len(matrix)+1
        n=len(matrix[0])+1
        self.sums=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                self.sums[i][j]=matrix[i-1][j-1]+self.sums[i-1][j]+self.sums[i][j-1]-self.sums[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1, row2, col2=row1+1,col1+1,row2+1,col2+1
        return self.sums[row2][col2]-self.sums[row2][col1-1]-self.sums[row1-1][col2]+self.sums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

