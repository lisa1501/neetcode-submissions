class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) +1

        fre_list = [[] for i in range(len(nums)+1)]
        
        for num in count:
            idx= count[num]
            fre_list[idx].append(num)

        result =[]
        for i in range(len(fre_list)-1, -1, -1):
            for num in fre_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result