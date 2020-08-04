# Source : https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
# Author : Haiyung
# Date   : 2020-07-30


'''
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
'''


def min_depth(root):
    if not root.val:
        return 0
    if not root.left.val:
        return min_depth(root.right) + 1
    if not root.right.val:
        return min_depth(root.left) + 1
    return min(min_depth(root.left), min_depth(root.right)) + 1


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def creat_tree(root, arr, index, length):
    # 完全二叉树
    if index < length:
        root.val = arr[index]
        root.left = creat_tree(TreeNode(None), arr, 2 * index + 1, length)
        root.right = creat_tree(TreeNode(None), arr, 2 * index + 2, length)
    return root


tree = TreeNode(None)
root = creat_tree(tree, [1, 2], 0, 2)
n = min_depth(root)
print(n)
