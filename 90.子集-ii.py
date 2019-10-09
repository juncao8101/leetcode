#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (57.06%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    13.4K
# Total Submissions: 23.3K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res,cur=[[]],[]
        if not nums:
            return res
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                cur=[item+[nums[i]] for item in cur]
                                #这里的cur表示上一次添加的数组
                                #如果碰到了相同元素，为了避免添加重复的子集，不能直接和res相加
                                #应该只在上一次的基础上加新东西，然后再加到res里面
            else:
                cur=[item+[nums[i]] for item in res]
            res+=cur
        return res
