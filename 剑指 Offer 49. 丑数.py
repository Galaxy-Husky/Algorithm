class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # # 1. 动态规划 三指针 O(N) O(N)
        # dp = [1]*n
        # a = b = c = 0
        # for i in range(1, n):
        #     n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
        #     dp[i] = min(n2, n3, n5)
        #     if dp[i] == n2:
        #         a += 1
        #     if dp[i] == n3:
        #         b += 1
        #     if dp[i] == n5:
        #         c += 1
        # return dp[-1]

        # 2. 最小堆 O(NlogN) O(N)
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n):
            cur = heapq.heappop(heap)
            if i == n-1:
                return cur
            for factor in factors:
                tmp = cur * factor
                if tmp not in seen:
                    seen.add(tmp)
                    heapq.heappush(heap, tmp)
