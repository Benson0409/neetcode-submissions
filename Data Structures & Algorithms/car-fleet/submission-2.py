class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 由快到慢的車子
        cars = sorted(zip(position,speed),reverse =True)
        
        currentTime = 0
        fleet = 0

        for p ,s in cars:
            time = (target-p)/s

            if time > currentTime:
                fleet += 1
                currentTime = time
            

        return fleet



       