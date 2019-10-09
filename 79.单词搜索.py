#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (38.96%)
# Likes:    210
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 51.6K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
# 
#
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board,r,c,word):
                    return True
        return False
    def dfs(self, board,r,c,word):
        if len(word)==0:return True
        if (not 0<=r<=len(board)-1) or (not 0<=c<=len(board[0])-1) or word[0]!=board[r][c]:
            return False
        temp=board[r][c]
        board[r][c]='#'
        res=self.dfs(board,r-1,c,word[1:]) or self.dfs(board,r,c-1,word[1:])\
        or self.dfs(board,r+1,c,word[1:]) or self.dfs(board,r,c+1,word[1:])
        board[r][c]=temp
        return res
