class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        n = 0
        long = 0

        for i in range(len(s)):
            while s[i] in s_set:
                s_set.remove(s[n])
                n+=1
            s_set.add(s[i])
            long = max(long,len(s_set))
            
        
        return long