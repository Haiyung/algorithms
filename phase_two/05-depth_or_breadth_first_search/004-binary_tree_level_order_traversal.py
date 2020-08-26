# Source : https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Author : Haiyung
# Date   : 2020-08-26
# Name   : 二叉树的层序遍历（重要！！！）

'''二叉树的层序遍历

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
'''


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
root = creat_tree(tree, [4, 2, 7, 1, 3, 8], 0, 6)


def level_order(root):
    visited, queue = set(), []
    queue.append(root)
    result = []

    while queue:
        node = queue.pop()
        visited.add(node)
        result.append(node.val)
        if node.left.val:
            queue.insert(0, node.left)
        if node.right.val:
            queue.insert(0, node.right)
    return result


ret = level_order(root)
print(ret)
