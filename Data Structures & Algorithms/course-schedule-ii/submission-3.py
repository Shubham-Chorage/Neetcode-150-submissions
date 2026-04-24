from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        course_dict = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            course_dict[course].append(pre)
            indegree[pre] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        result = []
        finish = 0

        while q:
            course = q.popleft()
            result.append(course)
            finish += 1

            for c in course_dict[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        if finish != numCourses:
            return []

        return result[::-1]
            
            

