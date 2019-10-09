#
# @lc app=leetcode.cn id=86 lang=python
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (52.43%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 28.5K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
# 
# 你应当保留两个分区中每个节点的初始相对位置。
# 
# 示例:
# 
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val<x:
                l1.next = head
                l1=l1.next
            else:
                l2.next = head
                l2=l2.next
            head=head.next
        l2.next = None
        l1.next = h2.next
        return h1.next
        


