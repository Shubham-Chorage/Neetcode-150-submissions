class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        s_len = len(s)
        res_len = 0

        for i in range(s_len):

            l,r = i,i
            while l >= 0 and r < s_len and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            l,r = i, i + 1
            while l >= 0 and r < s_len and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                l -= 1
                r += 1

        return res