class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count ={}
        max_num = 0
        l = 0
        long = 0 

        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
            max_num = max(max_num,count[s[i]])

            while i - l - max_num +1 > k:
                count[s[l]] -= 1
                l += 1

            long = max(long,i-l+1)

        return long