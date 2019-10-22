#
# @lc app=leetcode.cn id=16 lang=python
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.64%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    41.8K
# Total Submissions: 100.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    return sum
                if abs(sum-target)<abs(result-target):
                    result=sum
                if sum<target:
                    j+=1
                else:
                    k-=1
        return result


