class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = defaultdict(list)
        for i, num in enumerate(nums):
            count[num].append(i)

        print(count)
        res = 0
        for num in count:
            n = len(count[num])
            if n >= 2:
                res += (n * (n - 1))//2
        return res

        