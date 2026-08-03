class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Shortest Path (Unweighted BFS)
        # early return -1, if 0000 in set(deadends)
        # initialize a set with 0000 
        # initialize a queue, with [0000, 0] => [state, steps]
        # while queue,
        # popleft => state, steps 
        # if state same with target, return steps
        # loop through in range 4,
        # cur digit is state[i]
        # state[i] increase by 1, or decrease by 1 
        # new digit => state[i] += [1,-1], % 10 ex: (9+1) =10%10=0
        # new state : state[:i] + new digit + state[i+1:]
        # if we didn't visit new state yet, add it to visited, queue store new state and steps+1
        # loop through queue is done, return -1
        # Time: O(d^m + m), Space: O(d^n)
        # d => the num of 0-9, m => the num of deadends, n => the num of wheels(4), 
        deadends = set(deadends)

        if "0000" in deadends: 
            return -1

        visited = set()
        visited.add("0000")
        q = deque([("0000", 0)])

        while q:
            state, steps = q.popleft()
            if state == target:
                return steps

            for i in range(4):
                cur_digit = int(state[i])
                for move in [-1, 1]:
                    new_digit = cur_digit + move
                    new_digit %= 10

                    new_state = state[:i] + str(new_digit) + state[i+1:]

                    if new_state not in visited and new_state not in deadends:
                        visited.add(new_state)
                        q.append((new_state, steps + 1))

        return -1
                



    



        