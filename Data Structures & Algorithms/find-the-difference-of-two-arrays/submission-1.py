class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1,n2 = [],[]
        result = []
        first = set(nums1)
        second = set(nums2)
        for i in first:
            if i not in second:
                n1.append(i)
        for j in second:
            if j not in first:
                n2.append(j)
        
        result.append(n1)
        result.append(n2)
        return result
