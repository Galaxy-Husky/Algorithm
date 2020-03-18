#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (42.65%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    8.2K
# Total Submissions: 19.1K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 设计一个支持以下两种操作的数据结构：
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
# 
# 示例:
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# 说明:
# 
# 你可以假设所有单词都是由小写字母 a-z 组成的。
# 
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.child = {}
        self.isword = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for w in word:
            if w not in cur.child:
                cur.child[w] = TrieNode()
            cur = cur.child[w]
        cur.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(node, word):
            if not word:
                return node.isword
            if word[0] == '.':
                for n in node.child.values():
                    if dfs(n, word[1:]):
                        return True
                return False
            else:
                if word[0] not in node.child:
                    return False
                node = node.child[word[0]]
                return dfs(node, word[1:])

        node = self.root
        return dfs(node, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

