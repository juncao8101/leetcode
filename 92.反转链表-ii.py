#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (46.56%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    20.4K
# Total Submissions: 43.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
# 
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#和前面一样，p要在外面，tail始终指向下一个移动的目标
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n: return head
        p =tail= ListNode(0)
        p.next= head
        head=p
        for i in range(1,n+1):  #定好起始位置，在这里起始是第一个节点，那么i起始应该设置为1
            if i<m:
                p=p.next
            elif i==m:
                tail=p.next
            else:
                temp=ListNode(0)
                temp=tail.next
                tail.next=tail.next.next
                temp.next=p.next
                p.next=temp
        return head.next

