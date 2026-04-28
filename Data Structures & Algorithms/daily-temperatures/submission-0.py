class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in  range(len(temperatures)):

            while stack and  temperatures[i] > temperatures[stack[-1]]:

                previou_day = stack.pop()
                
                saved_day = i - previou_day

                answer[previou_day] = saved_day

            stack.append(i)



        return answer
