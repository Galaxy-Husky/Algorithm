class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 1. BFS O(N) O(N)
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
                res.append('null')
        return '['+','.join(res)+']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        i = 1
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if vals[i] != 'null':
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
        return root    