#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (38.21%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    28.9K
# Total Submissions: 75.2K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        new=[]
        for i in sorted(intervals):
            if new and i[0]<=new[-1][-1]:
                new[-1][-1]=max(i[-1],new[-1][-1])
            else:
                new.append(i)
        return new

