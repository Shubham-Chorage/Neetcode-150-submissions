class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):

            if start == len(s):
                result.append(path.copy())
                return

            for i in range(start, len(s)):
                substring = s[start:i+1]

                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result