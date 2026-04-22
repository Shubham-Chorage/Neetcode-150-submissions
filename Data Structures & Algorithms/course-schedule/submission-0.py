class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_dict = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            course_dict[course].append(prereq)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if course_dict[course] == []:
                return True

            visiting.add(course)

            for prereq in course_dict[course]:
                if not dfs(prereq):
                    return False
                
            visiting.remove(course)
            course_dict[course] = []
            return True

        for c in range(numCourses):
                if not dfs(c):
                    return False
        return True