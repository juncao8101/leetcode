#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (62.13%)
# Likes:    283
# Dislikes: 0
# Total Accepted:    39.4K
# Total Submissions: 63.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        front=ListNode(0)
        front.next=head
        newhead=front
        while front.next and front.next.next:   #成对就交换，有落单的不用管
            a=front.next
            b=a.next
            front.next,b.next,a.next=b,a,b.next #逗号表达式的原理是，右边一起打包存入一个新元组，然后给右边，因此不用担心顺序问题

            front=a     #更新front
        return newhead.next

