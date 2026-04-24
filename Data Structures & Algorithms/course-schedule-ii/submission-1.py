from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        course_dict = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            indegree[pre] += 1
            course_dict[course].append(pre)

        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, output= 0, []

        while q:
            node = q.popleft()  
            output.append(node)
            finish += 1
            for nei in course_dict[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []
        return output[::-1]  