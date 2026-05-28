class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course = defaultdict(list)
        course_count = [0]*numCourses

        for second,first in prerequisites:
            course[first].append(second)
            course_count[second] += 1

        bus = deque()

        for i in range(len(course_count)):
            if course_count[i] == 0:
                bus.append(i)
        classes_taken = 0

        while bus:
            current = bus.popleft()
            classes_taken += 1

            for i in course[current]:
                course_count[i] -= 1
                if  course_count[i] == 0:
                    bus.append(i)


        return classes_taken == numCourses

        