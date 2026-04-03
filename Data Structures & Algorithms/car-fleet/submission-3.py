class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []

        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            pairs.append((position[i],time))

        pairs.sort(reverse = True)

        stack = []

        for pos,time in pairs:
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)
