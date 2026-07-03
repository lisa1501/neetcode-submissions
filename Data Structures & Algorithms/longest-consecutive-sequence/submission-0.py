class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                #{2:1} 
                #{2:1, 20:1} 
                #{2:1, 20:1, 4:1} 
                #{2:1, 20:1, 4:1, 10:1} 
                #{2:1, 20:1, 4:1, 10:1, 3:3}
                    #{2:3, 20:1, 4:3, 10:1, 3:3}
                #{2:3, 20:1, 4:3, 10:1, 3:3, 5:4}
                    #{2:4, 20:1, 4:3, 10:1, 3:3, 5:4}
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        print(mp)
        return res
        