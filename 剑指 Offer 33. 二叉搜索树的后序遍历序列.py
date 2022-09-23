class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # # 1. 递归 O(N^2) O(N)
        # def recur(i, j):
        #     if i >= j:
        #         return True
        #     p = i
        #     while postorder[p] < postorder[j]:
        #         p += 1
        #     mid = p
        #     while postorder[p] > postorder[j]:
        #         p += 1
        #     return p == j and recur(i, mid-1) and recur(mid, j-1)

        # return recur(0, len(postorder)-1)

        # 2. 单调栈 O(N) O(N)
        stack = []
        root = float('inf')
        for i in range(len(postorder)-1, -1, -1):
            if postorder[i] > root:
                return False
            while stack and postorder[i] < stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
