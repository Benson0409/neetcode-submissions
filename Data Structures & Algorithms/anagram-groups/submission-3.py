class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = {}
        
        for s in strs:
            strs_key = tuple(sorted(s))
            if strs_key not in answer:
                answer[strs_key] = []

            answer[strs_key].append(s)

        return list(answer.values())
                