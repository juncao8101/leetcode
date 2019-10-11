#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#
# https://leetcode-cn.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (38.06%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 30.2K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
# 
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
# 
# 示例:
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# 运行你的函数后，矩阵变为：
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# 解释:
# 
# 被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O'
# 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
# 
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:return 
        m=len(board)
        n=len(board[0])
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j]='G'
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)  
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='G':
                    board[i][j]='O'
        


