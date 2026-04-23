class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        answer = []
        
        for i in range(len(nums)):
            
            if num[i] > 0:
                break
                
            if i > 0 and num[i] == num[i-1]:
                continue
                
            target = -num[i]
            r = len(num)-1
            l = 1 + i

            while l < r:
                current = num[l] + num[r]
                if current > target:
                    r -= 1
                elif current < target:
                    l += 1
                else:
                    answer.append([num[i], num[l], num[r]])

                    while l < r and num[l] == num[l+1]:
                        l += 1
                    
                    while l < r and num[r] == num[r-1]:
                        r -= 1
                        
                    l += 1
                    r -= 1

        return answer