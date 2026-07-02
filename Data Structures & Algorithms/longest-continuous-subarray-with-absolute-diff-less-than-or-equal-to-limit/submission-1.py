class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_que = deque()
        min_que = deque()

        longest = 0
        l = 0
        # nums=[24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,
        #       38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,
        #       50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,
        #       58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,
        #       81,55,8,95,39]
        # limit=87
        for r in range(len(nums)):
            
            while max_que and nums[r] > max_que[-1]:
                max_que.pop()
            max_que.append(nums[r])

            while min_que and nums[r] < min_que[-1]:
                    min_que.pop()
            min_que.append(nums[r])

            while max_que[0] - min_que[0] > limit:
                if nums[l] == max_que[0]:
                    max_que.popleft()

                if nums[l] == min_que[0]:
                    min_que.popleft()

                l += 1
            longest = max(longest, r -l + 1)

        return longest