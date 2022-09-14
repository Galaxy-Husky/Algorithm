class Solution:
    def reverseWords(self, s: str) -> str:
        # # 1. python O(N) O(N)
        # return ' '.join(reversed(s.split()))

        # 2. 自行编写函数 O(N) O(N)
        def trim_spaces(s:str):
            left, right = 0, len(s) - 1
            while left <= right and s[left] == ' ':
                left += 1
            while left <= right and s[right] == ' ':
                right -= 1
            
            res = []
            while left <= right:
                if s[left] != ' ':
                    res.append(s[left])
                elif res[-1] != ' ':
                    res.append(s[left])
                left += 1
            return res
        
        def reverse(l:list, left, right):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left+1, right-1
        
        def reverse_word(l:list):
            start, right = 0, len(l) - 1
            end = start
            while start <= right:
                while end <= right and l[end] != ' ':
                    end += 1
                else:
                    reverse(l, start, end-1)
                    start = end + 1
                    end += 1

        l = trim_spaces(s)
        reverse(l, 0, len(l)-1)
        reverse_word(l)
        return ''.join(l)