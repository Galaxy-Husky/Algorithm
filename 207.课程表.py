#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode-cn.com/problems/course-schedule/description/
#
# algorithms
# Medium (49.19%)
# Likes:    251
# Dislikes: 0
# Total Accepted:    27K
# Total Submissions: 54.3K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
# 
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
# 
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
# 
# 
# 
# 示例 1:
# 
# 输入: 2, [[1,0]] 
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
# 
# 示例 2:
# 
# 输入: 2, [[1,0],[0,1]]
# 输出: false
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
# 
# 
# 
# 提示：
# 
# 
# 输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
# 你可以假定输入的先决条件中没有重复的边。
# 1 <= numCourses <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, pre in prerequisites:
            indegree[cur] += 1
            adjacency[pre].append(cur)

        # # 1. 拓扑排序 BFS O(M+N) O(M+N)
        # q = []
        # for i in range(numCourses):
        #     if not indegree[i]:
        #         q.append(i)
        # while q:
        #     pre = q.pop(0)
        #     numCourses -= 1
        #     for cur in adjacency[pre]:
        #         indegree[cur] -= 1
        #         if not indegree[cur]:
        #             q.append(cur)
        # return not numCourses

        # 2.2 拓扑排序 DFS O(M+N) O(M+N)
        def dfs(i, flags):
            if flags[i] == -1:
                return True
            elif flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, flags):
                    return False
            flags[i] = -1
            return True
        
        flags = [0] * numCourses
        for i in range(numCourses):
            if not dfs(i, flags):
                return False
        return True

# @lc code=end

