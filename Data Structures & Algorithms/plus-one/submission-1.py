class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = ""
        output = []

        for digit in digits:
            res += str(digit)
        
        value = str(int(res) + 1)

        for i in value:
            output.append(i)

        return output


    