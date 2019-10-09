#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (35.37%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    21K
# Total Submissions: 59.3K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=imax=imin=nums[0]
        for i in range(1,len(nums)):
            candidates = (nums[i], imax * nums[i], imin * nums[i])
            imax = max(candidates)
            imin = min(candidates)
            res=max(res,imax)
        return res




