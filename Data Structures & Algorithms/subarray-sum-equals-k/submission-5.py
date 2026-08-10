class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time:O(n), space:O(n)
        res = 0
        cur_sum = 0
        prefixSums = {0: 1}

        for num in nums:
            cur_sum += num
            diff = cur_sum - k

            res += prefixSums.get(diff,0)
            prefixSums[cur_sum] = prefixSums.get(cur_sum, 0) + 1
            
        return res
        