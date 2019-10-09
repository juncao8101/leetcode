#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#
# https://leetcode-cn.com/problems/decode-ways/description/
#
# algorithms
# Medium (21.68%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    16.8K
# Total Submissions: 76.8K
# Testcase Example:  '"12"'
#
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。
# 
# 示例 1:
# 
# 输入: "12"
# 输出: 2
# 解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
# 
# 
# 示例 2:
# 
# 输入: "226"
# 输出: 3
# 解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 
# 
#
class Solution(object):
    def numDecodings(self, s):
        memo=[None]*len(s)
        def rec(memo,ind,s):
            if len(s)==1 and s[0]=='0':
                memo[ind]=0
                return 0
            if len(s)==1 or not s:return 1
            if s[0]=='0':
                memo[ind]=0
                return 0
            if memo[ind]:return memo[ind]
            m=0
            n=0
            m=rec(memo,ind+1,s[1:])
            if int(s[:2])<27:
                n=rec(memo,ind+2,s[2:])
            memo[ind]=m+n
            return memo[ind]
        return rec(memo,0,s)





