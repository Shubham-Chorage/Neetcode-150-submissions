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

        finish = 0
        output = []

        while q:
            course = q.popleft()
            output.append(course)
            finish += 1

            for c in course_dict[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        if finish != numCourses:
            return []

        return output[::-1]