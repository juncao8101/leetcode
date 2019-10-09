#
# @lc app=leetcode.cn id=61 lang=python
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (38.98%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 66.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p=head
        length=0
        while(p):
            p=p.next
            length+=1   #求链表长度

        k=k%length
        if length<=1 or k==0:return head   #边界情况    

        step=length-k-1
        p=head
        while(step):
            p=p.next
            step-=1     
        new_head=p.next
        p.next=None     #定位新的头结点,并且设置尾节点

        joint=new_head
        while(joint and joint.next):
            joint=joint.next
        joint.next=head         #拼接操作

        return new_head
        

