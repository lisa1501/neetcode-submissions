class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        ans = []

        for num in set_nums1:
            if num in set_nums2:
                ans.append(num)
        return ans
        