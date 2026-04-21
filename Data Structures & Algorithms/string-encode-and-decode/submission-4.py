class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = f"{len(strs[i])}#{strs[i]}" 
        return "".join(strs)
    def decode(self, s: str) -> List[str]:
        box = []
        i = 0
        while i < len(s):

            j = s.find("#",i)

            length = int(s[i:j])

            box.append(s[j+1:length+1+j])
            
            i = length+1+j
        return box

