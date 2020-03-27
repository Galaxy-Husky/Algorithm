class Solution:
    def reverseWords(self, s: str) -> str:
        """ #分词 反转 拼接
        return ' '.join(reversed(s.split())) """
        # 反转字符串 反转单词 去除空格
        def reverse_sentence(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            return arr

        def reverse_word(arr):
            i = j = 0
            n = len(arr)
            while i < n:
                while i < n and arr[i] == ' ':
                    i += 1
                j = i
                while j < n and arr[j] != ' ':
                    j += 1
                reverse_sentence(arr, i, j-1)
                i = j
            return arr

        def trim_spaces(arr):
            n = len(arr)
            i, j = 0, n-1
            while i < j and arr[i] == ' ':
                i += 1
            while i < j and arr[j] == ' ':
                j -= 1
            return arr[i:j+1]
        
        def remove_spaces(arr):
            if ''.join(arr) == ' ':
                return []
            res = [arr[0]]
            for i in range(1, len(arr)):
                if arr[i] == ' ' and res[-1] == ' ':
                    continue
                res.append(arr[i])
            return res

        if not s:
            return ''
        arr = list(s)
        arr = reverse_sentence(arr, 0, len(arr)-1)
        arr = reverse_word(arr)
        arr = trim_spaces(arr)
        res = remove_spaces(arr)
        return ''.join(res)