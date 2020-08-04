# Source : https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Author : Haiyung
# Date   : 2020-08-03
# Name   : 二叉树的最近公共祖先


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        if l:
            return l
        if r:
            return r
