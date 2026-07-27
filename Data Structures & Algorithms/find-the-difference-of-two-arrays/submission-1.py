class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[],[]]
        num1Set, num2Set = set(nums1), set(nums2)
        for num in num1Set:
            if num not in num2Set:
                ans[0].append(num)

        for num in num2Set:
            if num not in num1Set:
                ans[1].append(num)
            
        return ans
        