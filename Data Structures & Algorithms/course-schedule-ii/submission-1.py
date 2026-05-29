class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_count = numCourses*[0]
        course = defaultdict(list)
        answer = []

        for second,first in prerequisites:
            course[first].append(second)
            course_count[second] += 1

        bus = deque()

        for i in range(len(course_count)):
            if course_count[i] == 0:
                bus.append(i)
            

        while bus:
            current = bus.popleft()
            answer.append(current)
            for i in course[current]:
                course_count[i] -= 1
                if course_count[i] == 0:
                    bus.append(i)

        for i in course_count:
            if i != 0:
                return []
        return answer