class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # early return if source == target
        # hashmap, stop to list route idx, a bus stop stations on which routes
        # stop set, with source
        # route set, empty
        # queue store (stop, how many buses), (source, 0)
        # while q 
        # popleft, stop, buses, if stop == target, return buses
        # loop thru route in hashmap[stop]
        # if route not in route set, add it to route set
        # loop through route in routes
        # if route not in stop set, add it to stop set, add it to queue
        # if there is not route for source -> target, return -1
        # time: O(n) space O(n) n istotal number of stops across all routes

        if source == target:
            return 0

        stop_to_rout = defaultdict(list)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_rout[stop].append(route_idx)

        stop_set = set()
        stop_set.add(source)
        route_set = set()
        q = deque([(source, 0)])

        while q:
            stop, buses = q.popleft()
            if stop == target:
                return buses
            for route_idx in stop_to_rout[stop]:
                if route_idx not in route_set:
                    route_set.add(route_idx)

                    for stop in routes[route_idx]:
                        if stop not in stop_set:
                            stop_set.add(stop)
                            q.append((stop, buses + 1))
        return -1
                