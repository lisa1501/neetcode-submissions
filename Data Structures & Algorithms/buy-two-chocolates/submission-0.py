class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # sort prices
        # cost is sum of first two index price
        # if money <= cost, return lefover
        # could't buy cheapest two chocolate, return money
        # time: O(nlog) space: O(1)

        prices.sort()

        cost = prices[0] + prices[1]
        
        if money >= cost:
            return money - cost
        return money

        