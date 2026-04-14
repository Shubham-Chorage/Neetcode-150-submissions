class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        count = {}
        for num in hand:
            count[num] = count.get(num, 0) + 1

        for num in sorted(count):
            while count[num] > 0:
                for i in range(groupSize):
                    if count.get(num + i, 0) == 0:
                        return False
                    count[num + i] -= 1

        return True
