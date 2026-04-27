class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {"(":")","{":"}","[":"]"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):

            if s[i] in s_dict:
                stack.append(s[i])

            elif len(stack) == 0:
                return False

            elif s[i] == s_dict[stack[-1]]:
                stack.pop(-1)

            else:
                return False

        return len(stack) == 0
