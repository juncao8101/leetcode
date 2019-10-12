#
# @lc app=leetcode id=1202 lang=python
#
# [1202] Smallest String With Swaps
#
# https://leetcode.com/problems/smallest-string-with-swaps/description/
#
# algorithms
# Medium (40.57%)
# Likes:    162
# Dislikes: 7
# Total Accepted:    5K
# Total Submissions: 12.4K
# Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
#
# You are given a string s, and an array of pairs of indices in the string
# pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# 
# You can swap the characters at any pair of indices in the given pairs any
# number of times.
# 
# Return the lexicographically smallest string that s can be changed to after
# using the swaps.
# 
# 
# Example 1:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# 
# 
# Example 2:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# 
# Example 3:
# 
# 
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
# 
# 
#

# @lc code=start
import collections
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        class UF(object):
            def __init__(self,n):
                self.parent=list(range(n))
            def find(self,x):
                if self.parent[x]!=x:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            def union(self,x,y):
                self.parent[self.find(x)]=self.find(y)
        n=len(s)
        uf=UF(n)
        res=[]
        d=collections.defaultdict(list)
        for x,y in pairs:
            uf.union(x,y)
        for i in range(n):
            d[uf.find(i)].append(s[i])
        for i in range(n):
            d[i].sort(reverse=True)
        for i in range(n):
            res.append(d[uf.find(i)].pop())
        return ''.join(res)



        