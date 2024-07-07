import collections
from typing import List


class Solution:

    # Failed one test -- Speed
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def backTracking(tickets):
            nonlocal curr
            if not tickets: return True

            for i, val in enumerate(tickets):
                if val[0] == curr[-1]:
                    curr.append(val[1])
                    tmp = backTracking(tickets[:i]+tickets[i+1:])
                    if tmp: return True
                    curr.pop()
        res, curr = [], []
        start = "JFK"

        # Possible start candidates
        t_start = {}
        for i,t in enumerate(tickets):
            if t[0] == start:
                t_start[i] = t

        t_start = {k: v for k, v in sorted(t_start.items(), key=lambda item: item[1])}
        for i, ticket in t_start.items():
            curr = ticket
            if backTracking(sorted(tickets[:i] + tickets[i+1:])):
                return curr

# Failed test - Time limit
# print(Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","JFK"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"],["ATL","AAA"],["AAA","BBB"],["BBB","ATL"]]))

# Passed
# print(Solution().findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# print(Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))


class Solution2:

    # Failed one test -- Speed
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def backTracking(curr_airport):
            nonlocal curr, destinations
            if len(curr) == len(tickets) + 1: return True
            if curr_airport not in destinations: return False

            cur_destinations = destinations[curr_airport]
            for i, val in enumerate(cur_destinations):
                destinations[curr_airport].pop(i)
                curr.append(val)
                if backTracking(val) : return True
                destinations[curr_airport].insert(i, val)
                curr.pop()
            return False


        curr = ['JFK']
        destinations = {src:[] for src,_ in tickets}
        tickets.sort()
        for src, dst in tickets:
            destinations[src].append(dst)
        #destinations = {k: sorted(v, reverse=True) for k, v in sorted(destinations.items(), key=lambda item: item[1])}

        backTracking('JFK')
        return curr



    def findItineraryTraversal(self, tickets: List[List[str]]) -> List[str]:

        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,

        curr = []

        def traversal(src):
            nonlocal targets
            dests = targets[src]
            while dests:
                dest = dests.pop()
                traversal(dest)

            curr.append(src)
        traversal("JFK")
        return curr[::-1]


# Passed
print(Solution().findItinerary(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
print(Solution2().findItineraryTraversal(tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))

print(Solution().findItinerary(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
print(Solution2().findItineraryTraversal(tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))

