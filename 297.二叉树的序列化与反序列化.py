#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (44.35%)
# Likes:    145
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 36.3K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# 
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
# 
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
# 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
# 
# 示例: 
# 
# 你可以将以下二叉树：
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# 序列化为 "[1,2,3,null,null,4,5]"
# 
# 提示: 这与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
# 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
# 
# 说明: 不要使用类的成员 / 全局 / 静态变量来存储状态，你的序列化和反序列化算法应该是无状态的。
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #DFS 先序遍历
        def preorder(root):
            if not root:
                serial.append('#')
            else:
                serial.append(str(root.val))
                preorder(root.left)
                preorder(root.right)

        serial = []
        preorder(root)
        return ','.join(serial)

        """ # BFS
        if not root:
            return '[]'
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
        return ','.join(res) """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        """ # iter + next
        def build():
            s = next(serial)
            if s == '#':
                return None
            node = TreeNode(int(s))
            node.left = build()
            node.right = build()
            return node

        serial = iter(data.split(','))
        return build() """

        def build():
            val = data.pop(0)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        data = data.split(',')
        root = build()
        return root

        """ if data == '[]':
            return None
        data = data.split(",")
        i = 1
        root = TreeNode(int(data[0]))
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if data[i] != '#':
                node.left = TreeNode(int(data[i]))
                q.append(node.left)
            i += 1
            if data[i] != '#':
                node.right = TreeNode(int(data[i]))
                q.append(node.right)
            i += 1
        return root """
            


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

