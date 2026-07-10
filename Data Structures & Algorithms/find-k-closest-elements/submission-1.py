class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # [1, 3, 5]  x = 3, k = 1 => [3]
        # [1, 3, 5]  x = 3, k = 2 => [1, 3]
        # [1] , x = 3, k=2  => no a case

        # Input: arr = [2,4,5,8], k = 2, x = 6
        #                  l r
        #.            abs(6-2)> abs(6-8)  l + 1
        #             abs(6-4) <= abs(6-8) r -1
        # window length r - l + 1 >k
        # return arr[l:r]
        # time: O(n)
        # space: O(k)

        l = 0
        r = len(arr) - 1

        while r - l + 1 > k:
            if abs(x - arr[l]) > abs(x- arr[r]):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]



        