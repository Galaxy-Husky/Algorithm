#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (57.07%)
# Likes:    965
# Dislikes: 0
# Total Accepted:    263K
# Total Submissions: 460.8K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n' +
#  '[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) —— 将元素 x 推入栈中。
# pop() —— 删除栈顶的元素。
# top() —— 获取栈顶元素。
# getMin() —— 检索栈中的最小元素。
# 
# 
# 
# 
# 示例:
# 
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
# 
# 
# 提示：
# 
# 
# pop、top 和 getMin 操作总是在 非空栈 上调用。
# 
# 
#

# @lc code=start
class MinStack:
    # # 1. 辅助栈 O(1) O(N)

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #     self.min_stack = []


    # def push(self, val: int) -> None:
    #   self.stack.append(val)
    #   if not self.min_stack or val <= self.min_stack[-1]:
    #     self.min_stack.append(val)


    # def pop(self) -> None:
    #   if self.stack.pop() == self.min_stack[-1]:
    #     self.min_stack.pop()


    # def top(self) -> int:
    #   return self.stack[-1]


    # def getMin(self) -> int:
    #   return self.min_stack[-1]

    # 2. 保存差值，不用额外空间 O(1) O(1)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = float('inf')


    def push(self, val: int) -> None:
      if not self.stack:
        self.min_value = val
      diff = val - self.min_value
      self.stack.append(diff)
      self.min_value = min(val, self.min_value)

    def pop(self) -> None:
      p = self.stack.pop()
      if p < 0:
        self.min_value = self.min_value - p

    def top(self) -> int:
      top = self.stack[-1]
      if top < 0:
        return self.min_value
      else:
        return top + self.min_value

    def getMin(self) -> int:
      return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

