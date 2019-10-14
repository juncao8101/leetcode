#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (71.57%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    46.1K
# Total Submissions: 64.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def backtrack(nums,path):
            if not nums:
                res.append(path)
            for i in xrange(len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        res=[]
        backtrack(nums,[])
        return res
