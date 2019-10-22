#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (56.64%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 39.6K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        candidates.sort()
        self.backtracking(candidates,0,target,[],res)
        return res
    def backtracking(self,nums,start,target,path,res):
        if target == 0:
            res.append(path)
            return
        for i in xrange(start,len(nums)):
            if i>start and nums[i] == nums[i-1]:
                continue
            if nums[i]>target:
                break
            self.backtracking(nums,i+1,target-nums[i],[nums[i]]+path,res)
    
