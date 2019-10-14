#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (53.97%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 41.6K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums,path):
            if not nums:
                res.append(path)
                return
            for i in xrange(len(nums)):
                if i>=1 and nums[i]==nums[i-1]:
                    continue
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])
        res=[]
        nums.sort()
        backtrack(nums,[])
        return res
