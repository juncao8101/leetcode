#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (58.80%)
# Likes:    283
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 91.8K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l,r,k=0,len(nums)-1,k-1
        while 1:
            index=self.partition(nums,l,r)
            if index==k:
                return nums[index]
            elif index>k:
                r=index-1
            else:
                l=index+1
        
    def partition(self,nums,l,r):
        mid=nums[l]
        while l<r:
            while l<r and nums[r]<=mid:
                r-=1
            nums[l]=nums[r]
            while l<r and nums[l]>mid:
                l+=1
            nums[r]=nums[l]
        nums[l]=mid
        return l
    
        
# @lc code=end

