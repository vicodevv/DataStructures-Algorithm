class Solution:
    def reverseWords(self, s: str) -> str:
        res, n = '', len(s)
        i = 0
        while i < n:
            while i < n and s[i] == ' ':
                i+=1
            if i >= n:
                break
            j=i+1
            while j < n and s[j] != ' ':
                j+=1
            substring = s[i:j]
            if len(res) == 0:
                res = substring
            else:
                res = substring + ' ' + res
            i = j+1
        return res
