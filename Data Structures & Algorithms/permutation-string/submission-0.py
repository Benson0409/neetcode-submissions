class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        for i in range(len(s2)-len(s1)+1):
            current = s2[i:len(s1)+i]
            print(current)
            if sorted(s1) == sorted(current):
                return True
        return False