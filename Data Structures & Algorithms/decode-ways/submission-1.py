class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == '0':
            return 0

        old = 1
        new = 1

        for i in range(1, len(s)):
            total = 0

            if s[i] != '0':
                total += new

            if 10 <= int(s[i-1:i+1]) <= 26:
                total += old

            old = new
            new = total

            print(new)
            print(total)

        return new
