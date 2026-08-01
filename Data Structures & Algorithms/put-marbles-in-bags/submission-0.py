class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # create an empty list to store weights[i] + weights[i+1]
        # sort the list
        # min is sum of first k-1 weights
        # max is sum of last k-1 weights
        # return diff of max-min
        # Time: O(nlog n) Space: O(n)
        
        if k == 1:
            return 0

        pairs = []

        for i in range(len(weights)-1):

            pairs.append(
                weights[i] + weights[i+1]
            )


        pairs.sort()

        print(pairs)
        maximum = sum(
            pairs[-(k-1):]
        )

        minimum = sum(
            pairs[:k-1]
        )


        return maximum - minimum
        