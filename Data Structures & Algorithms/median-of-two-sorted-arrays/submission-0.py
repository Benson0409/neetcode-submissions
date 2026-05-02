class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums = nums1 + nums2
        
        clean_nums = sorted(nums)
        left = 0
        right = len(clean_nums)-1

        if right % 2 ==0:
            return float(clean_nums[right//2])
        else:
            answer = clean_nums[right//2] + clean_nums[(right//2)+1]
            return answer/2