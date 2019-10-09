#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (43.63%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    18.6K
# Total Submissions: 42.6K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
# 
# 示例 1:
# 
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
# 
# 示例 2:
# 
# 输入: 1->1->1->2->3
# 输出: 2->3
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        p=ListNode(0)
        p.next = head
        head=p
        left=ListNode(0)
        right=ListNode(0)
        while p.next:
            left=right=p.next
            while right.next and right.val == right.next.val:
                right=right.next
            if left==right:
                p=p.next
            else:
                p.next=right.next
        return head.next



        

