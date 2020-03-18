#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (39.14%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 26.4K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
  '["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
# 
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 示例:
# 
# 输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"]
# 
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
# 
# 提示:
# 
# 
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
# 
# 
#

# @lc code=start
class TrieNode:
  def __init__(self):
    self.child = {}
    self.word = False

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, word):
    cur = self.root
    for w in word:
      if w not in cur.child:
        cur.child[w] = TrieNode()
      cur = cur.child[w]
    cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
      # 字典树 Trie + DFS
      def dfs(board, node, i, j, path):
        if node.word:
          res.append(path)
          node.word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
          return
        tmp = board[i][j]
        if tmp not in node.child:
          return
        node = node.child[tmp]
        board[i][j] = '#'
        dfs(board, node, i+1, j, path+tmp)
        dfs(board, node, i-1, j, path+tmp)
        dfs(board, node, i, j+1, path+tmp)
        dfs(board, node, i, j-1, path+tmp)
        board[i][j] = tmp
        
      res = []
      trie = Trie()
      node = trie.root
      for word in words:
        trie.insert(word)
      for i in range(len(board)):
        for j in range(len(board[0])):
          dfs(board, node, i, j, '')
      return res
      
# @lc code=end

