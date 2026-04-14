class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # We need to count the freq and have a dictionary
        # We check if the groupSize of next numbers exist for the start and proceed

        if len(hand) % groupSize != 0:
            return False

        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        print(count)

        for num in sorted(count):
            while count[num] > 0:
                for val in range(groupSize):
                    if count.get(num + val, 0) == 0:
                        return False
                    count[num + val] -= 1

        return True