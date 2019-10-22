#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (71.78%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    40.6K
# Total Submissions: 56.5K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        def backward(s='',left=0,right=0):
            if len(s)==2*n:
                ans.append(s)
                return 
            if left<n:
                backward(s+'(',left+1,right)
            if right<left:
                backward(s+')',left,right+1)
        backward()
        return ans


