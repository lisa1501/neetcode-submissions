class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_que = deque()
        min_que = deque()

        longest = 0
        l = 0
        for r in range(len(nums)):
            while max_que and max_que[-1] < nums[r]:
                max_que.pop()
            max_que.append(nums[r])

            while min_que and min_que[-1] > nums[r]:
                min_que.pop()
            min_que.append(nums[r])

            while max_que[0] - min_que[0] > limit:
                if nums[l] == max_que[0]:
                    max_que.popleft()

                if nums[l] == min_que[0]:
                    min_que.popleft()

                l += 1
            longest = max(longest, r - l + 1)
        return longest