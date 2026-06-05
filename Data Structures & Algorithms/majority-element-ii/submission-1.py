class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        res = []
        for num in count:
            if count[num] > len(nums)//3:
                res.append(num)
        return res

        print(count)


        