from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        way=defaultdict(list)
        n=len(tickets)
        answer=[]

        for ticket in sorted(tickets):
            _from,_to =ticket
            way[_from].append(_to)

        def dfs(f):
            while way[f]:
                dfs(way[f].pop(0))
            answer.append(f)

        dfs('JFK')
        return answer[::-1]