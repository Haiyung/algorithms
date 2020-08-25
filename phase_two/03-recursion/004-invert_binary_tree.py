# Source : https://leetcode-cn.com/problems/invert-binary-tree/description/
# Author : Haiyung
# Date   : 2020-07-30


'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


def invert_tree(root):
    def helper(root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        helper(root.left)
        helper(root.right)
    helper(root)
    return root


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
