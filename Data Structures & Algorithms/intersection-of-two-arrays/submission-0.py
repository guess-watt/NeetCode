class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        if len(nums1) > len(nums2):
            for i in nums2:
                if i in nums1:
                    result.add(i)
            return list(result)
        else:
            for j in nums1:
                if j in nums2:
                    result.add(j)
            return list(result)
