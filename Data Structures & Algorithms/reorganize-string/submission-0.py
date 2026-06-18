class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        #{"a":1, "x":1, "y":2}

        heap = [(-cnt, ch) for ch, cnt in freq.items()] 
        heapq.heapify(heap) #[(-2,y),(-1,a),(-1,x)]

        result = []
        prev = None  # (cnt, ch)

        while heap or prev:

            if prev and not heap:
                return ""

            cnt, ch = heapq.heappop(heap) #-2,y

            result.append(ch) #[y]
            cnt += 1  # used one occurrence cnt=-1

            # push previous back into heap
            if prev:
                heapq.heappush(heap, prev)
                prev = None

            # hold current if still remaining
            if cnt < 0:
                prev = (cnt, ch) #prev = (-1,y)

        return "".join(result)
        