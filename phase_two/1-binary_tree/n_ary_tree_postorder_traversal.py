# Source : https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
# Author : Haiyung
# Date   : 2020-07-25

# N叉树的后序遍历


def postorder(root):
    res = []

    def dfs(root):
        if root:
            for i in root.children:
                dfs(i)
            res.append(root.val)

    dfs(root)
    return res
