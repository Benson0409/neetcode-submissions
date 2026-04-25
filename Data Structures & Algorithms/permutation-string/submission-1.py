class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        example = {}
        answer = {}
        l = 0

        for i in range(len(s1)):
            example[s1[i]] = example.get(s1[i],0)+1

        for i in range(len(s2)):

            answer[s2[i]] = answer.get(s2[i],0) +1

            if i >= len(s1):
                old_char = s2[l]
                
                if answer[old_char] > 1:
                    answer[old_char] -= 1
                else:
                    del answer[old_char]
                l += 1
            
            if answer == example:
                return True
            

        return False