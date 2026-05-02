class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1

        need_num = (len(nums1) + len(nums2) + 1) // 2

        left = 0
        right = len(nums1)

        while left <= right:
            mid = (right+left)//2
            cut1 = mid
            cut2 = need_num - cut1

            if cut1 == 0:
                left1 = float("-inf")
            else:
                left1 = nums1[cut1-1]

            if cut1 == len(nums1):
                right1 =  float("inf")
            else:
                right1 = nums1[cut1]

            if cut2 == 0:
                left2 = float("-inf")
            else:
                left2 = nums2[cut2-1]

            if cut2 == len(nums2):
                right2 =  float("inf")
            else:
                right2 = nums2[cut2]


            if left1<=right2 and left2<=right1:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(left1,left2)
                else:
                    return (max(left1,left2) + min(right1,right2))/2

            elif left1 > right2:
                right = cut1 - 1
            else:
                left = cut1+1 
