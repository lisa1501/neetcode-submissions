class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count of nums
        # initialize a list [[] * len(nums)+1]
        # loop through the count of nums, add key to list[idx] idx = value 
        # initialize a list res []
        # loop through list from back to front,
        # res append ele, k decrease by 1
        # if k is 0, return res
        # return res
        # Time:O(n) space:(n) n is len of nums

        count = Counter(nums)

        freq = [[] for i in range(len(nums) + 1)]

        for key in count:
            idx = count[key]
            freq[idx].append(key)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                k -= 1

                if k == 0:
                    return res
        return res
