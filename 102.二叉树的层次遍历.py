#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (59.24%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    51.3K
# Total Submissions: 86.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

recursive:

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def helper(root,level):
            if len(res)==level:
                res.append([])
            res[level].append(root.val)
            if root.left:
                helper(root.left,level+1)
            if root.right:
                helper(root.right,level+1)

        if not root:return []
        res=[]
        helper(root,0)
        return res

iterate:

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        parents,res=[root],[]
        flag=0
        while parents:
            sublist=[]
            children=[]
            for parent in parents:
                sublist.append(parent.val)
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
            parents=children
            res.append(sublist)
        return res
        

# @lc code=end

