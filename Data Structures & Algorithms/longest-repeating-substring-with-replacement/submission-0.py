class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxf = 0
        l = 0
        max_len = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1
            maxf = max(maxf,count[s[i]])

            while (i - l + 1) - maxf > k:
                count[s[l]] -= 1  
                l += 1            
                
            max_len = max(max_len, i - l + 1)
            
        return max_len