#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (42.78%)
# Likes:    201
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 46.2K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True              #这里的dp[0]=True并不表示位置，而是表示一种初始状态
        for i in range(1,n+1):
            for word in wordDict:       #同一个位置可能有好几种到达的方式，所以要遍历wordDict
                if i>=len(word) and dp[i-len(word)] and s[i-len(word):i]==word:
                    dp[i]=True          #dp[i]为True表示从头分割的话可以分割到第i个位置来
                                        
        return dp[-1]
        

