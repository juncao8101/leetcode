#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (66.02%)
# Likes:    245
# Dislikes: 0
# Total Accepted:    16.6K
# Total Submissions: 25K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
        board=[['.' for i in range(n)] for i in range(n)]
        col=[True]*n
        diag1=[True]*(2*n-1)    #左下到右上的许多对角线，从左上到右下从0开始编号
        diag2=[True]*(2*n-1)    #左上到右下的许多对角线，从左下到右上从0开始编号

        def updateBoard(x,y,n,flag):
            col[x]=flag
            diag1[x+y]=flag
            diag2[x-y+n-1]=flag
            board[y][x]='Q' if not flag else '.'
        def available(x,y):
            return col[x] and diag1[x+y] and diag2[x-y+n-1]
        def nqueens(y,n):
            if y>=n:
                temp=[]
                for i in range(n):
                    temp.append(''.join(board[i]))
                res.append(temp)
                return
            for x in range(n):  #同一排挨个试
                if not available(x,y):
                    continue
                updateBoard(x,y,n,False)    #直到出现一个可以填Q的
                nqueens(y+1,n)  #进行下一行的选取
                updateBoard(x,y,n,True)     #再调整回来
        nqueens(0,n)
        return res 
# @lc code=end

