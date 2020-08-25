# Source : https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
# Author : Haiyung
# Date   : 2020-07-25

# N叉树的前序遍历


def preorder(root):
    res = []

    def dfs(root):
            if root:
                res.append(root.val)
                for i in root.children:
                    dfs(i)
    dfs(root)
    return res
