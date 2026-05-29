class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hm = {}
        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        print(hm)

        res =[]
        for num in hm:
            if hm[num] > len(nums) // 3:
                res.append(num)
        return res

        