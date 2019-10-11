#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (49.75%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    8.1K
# Total Submissions: 16.3K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
# 
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=1:return 0
        if n==2:
            count=prices[1]-prices[0]
            return count if count>0 else 0
        yes=[0]*n
        no=[0]*n

        yes[0]=-prices[0]
        no[1]=max(yes[0]+prices[1],no[0])
        yes[1]=max(no[0]-prices[1],yes[0])
                                        #处理前两个数据
        for i in range(2,n):
            no[i]=max(yes[i-1]+prices[i],no[i-1])
            yes[i]=max(no[i-2]-prices[i],yes[i-1])
        return max(no[-1],yes[-1])  

