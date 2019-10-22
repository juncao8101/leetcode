#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (37.59%)
# Likes:    212
# Dislikes: 0
# Total Accepted:    34.2K
# Total Submissions: 90.7K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 如果数组中不存在目标值，返回 [-1, -1]。
# 
# 示例 1:
# 
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 
# 示例 2:
# 
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_search(nums, target):
            left=0
            right=len(nums)-1
            while left <= right:
                mid=(left+right)/2
                if nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return left
        def right_search(nums,target):
            left=0
            right=len(nums)-1
            while left <= right :
                mid = (left+right)/2
                if nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return right
        l,r=left_search(nums, target),right_search(nums,target)
        return [l,r] if l<=r else [-1,-1]

        

