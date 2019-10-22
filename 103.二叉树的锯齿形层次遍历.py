#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (52.31%)
# Likes:    106
# Dislikes: 0
# Total Accepted:    20.8K
# Total Submissions: 39.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回锯齿形层次遍历如下：
# 
# [
# ⁠ [3],
# ⁠ [20,9],
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

class Solution(object):
    def zigzagLevelOrder(self, root):
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

            if flag==1:
                sublist.reverse()
                flag=0
            else:
                flag=1
                
            res.append(sublist)
        return res
# @lc code=end

