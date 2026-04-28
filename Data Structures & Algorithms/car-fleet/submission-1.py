class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 由快到慢的車子
        cars = sorted(zip(position,speed),reverse =True)
        stack = []

        for p ,s in cars:
            stack.append((target-p)/s)

            while len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



       