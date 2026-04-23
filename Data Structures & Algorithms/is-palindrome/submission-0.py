class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([char.lower() for char in s if char.isalnum()])

        n = len(new_s) // 2
        print(new_s)
        for i in range(n):
            if new_s[i] != new_s[-1-i]:
                return False
        return True