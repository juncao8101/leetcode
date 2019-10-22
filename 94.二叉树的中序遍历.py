#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (67.86%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    59.4K
# Total Submissions: 87.5K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res=[]
        def helper(head):
            if head:
                helper(head.left)
                res.append(head.val)
                helper(head.right)
                #不能return啊 不然执行不下去了。。。。
        helper(root)
        return res


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack,res=[],[]
        while(root or stack):
            while(root):       #查看这个节点是否含有左分支
                stack.append(root)     #一路向左并将沿途节点压入堆栈
                root=root.left
            root=stack.pop()       #左子树处理完了就pop一个节点出来
            res.append(root.val)     #访问节点
            root=root.right         #转向右子树
        return res

        





