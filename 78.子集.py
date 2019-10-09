#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (74.75%)
# Likes:    344
# Dislikes: 0
# Total Accepted:    37.3K
# Total Submissions: 49.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#第一种方法：递归
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(0,[],nums,res)
        return res
    def dfs(self,index,path,nums,res):
        res.append(path)
        print(path)
        for i in xrange(index,len(nums)):
            self.dfs(i+1,path+[nums[i]],nums,res)

#第二种：列表推导式
class Solution(object):
    def subsets(self, nums):
        res=[[]]
        for num in nums:
            res+=[[num]+item for item in res]
        return res
