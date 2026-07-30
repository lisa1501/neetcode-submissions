class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        count = 0
    
        l = 0
        for r in range(len(grumpy)):
            if grumpy[r] == 1:
                count += customers[r]
            
            if r - l + 1 > minutes:
                if grumpy[l] == 1:
                    count -= customers[l]
                l += 1

            if r - l + 1 == minutes:
                ans = max(ans, count)
        print(ans)
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                ans += customers[i]

        return ans

    
        