class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # time:O(n), space:O(n)
        res = 0
        prefixSums = {0 : 1}
        cur_sum = 0

        for num in nums:
            cur_sum += num
            remain = cur_sum % k

            res += prefixSums.get(remain,0)
            prefixSums[remain] = prefixSums.get(remain,0)+1
        return res
        