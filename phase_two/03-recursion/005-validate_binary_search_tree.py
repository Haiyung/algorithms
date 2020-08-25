# Source : https://leetcode-cn.com/problems/validate-binary-search-tree/
# Author : Haiyung
# Date   : 2020-07-30


'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''


# 解法一：利用“BST定义”来逐一判断--递归调用
# 解法二：利用“BST中序遍历是递增”的这一特点


def is_valid_BST(root):
    boolean = recurse(root, float('-inf'),  float('inf'))
    print(boolean)


def recurse(root, lower, upper):
    if not root.val:
        return True
    if root.val <= lower or root.val >= upper:
        return False
    return (recurse(root.left, lower, root.val) and recurse(root.right, root.val, upper))


'''
def recurse(root, lower, upper):
    if not root.val:
        return True

    val = root.val
    if val <= lower or val >= upper:
        return False

    if not recurse(root.right, val, upper):
        return False
    if not recurse(root.left, lower, val):
        return False
    return True
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
is_valid_BST(root)
