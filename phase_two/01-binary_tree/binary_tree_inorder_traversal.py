# Source : https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# Author : Haiyung
# Date   : 2020-07-24

# 二叉树的中序遍历


'''
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]

进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def creat_tree(root, arr, index, length):
    # 完全二叉树
    if index < length:
        root.val = arr[index]
        root.left = creat_tree(root, arr, 2 * index + 1, length)
        root.right = creat_tree(root, arr, 2 * index + 2, length)
    return root


def inorder_traversal(root, res):
    if root:
        inorder_traversal(root.left, res)
        res.append(root.val)
        inorder_traversal(root.right, res)
