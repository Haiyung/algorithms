# https://www.cnblogs.com/-citywall123/p/11788764.html （满二叉树、完全二叉树概念解析）
# https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/ （用数组构建完全二叉树）


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
