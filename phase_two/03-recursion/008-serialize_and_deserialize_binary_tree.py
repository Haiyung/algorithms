# Source : https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
# Author : Haiyung
# Date   : 2020-07-30

'''二叉树的序列化与反序列化

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
'''
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])
        while queue:
            root = queue.popleft()
            if root.val:
                res.append(root.val)
                queue.extend([root.left, root.right])
            else:
                res.append('#')
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = [(TreeNode(v) if v != '#' else None) for v in eval(data)]
        i, j, n = 0, 1, len(nodes)
        while j < n:
            if nodes[i]:
                nodes[i].left = nodes[j]
                j += 1
                nodes[i].right = nodes[j]
                j += 1
            i += 1
        return nodes[0]


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
root = creat_tree(tree, [1, 2, 3, 4, 5, 6], 0, 6)
c = Codec()
ret = c.serialize(root)
print(ret)
