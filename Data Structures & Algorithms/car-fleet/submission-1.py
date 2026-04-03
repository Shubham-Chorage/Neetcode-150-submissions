class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []

        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            pairs.append((position[i],time))

        pairs.sort(reverse = True)

        count = 0
        max_time = 0

        for pos,time in pairs:
            if time > max_time:
                count += 1
                max_time = time

        return count
