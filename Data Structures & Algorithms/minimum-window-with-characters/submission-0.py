class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        example = {}
        answer = {}

        long = float("inf")
        short_bound = [-1,-1]
        
        l = 0

        for i in range(len(t)):
            example[t[i]] = example.get(t[i],0) + 1
        
        need,have = len(example),0

        for i in range(len(s)):
            new_char = s[i]
            answer[new_char] = answer.get(new_char,0) + 1

            if new_char in example and answer[new_char] == example[new_char]:
                have += 1

            while have == need:
                if long > min(long,i -l +1):
                    long  = min(long,i -l +1)
                    short_bound = [l,i]

                
                old_char = s[l]
                answer[old_char] -= 1

                if old_char in example and answer[old_char] < example[old_char]:
                    have -= 1
                l += 1

        return s[short_bound[0]:short_bound[1]+1]
