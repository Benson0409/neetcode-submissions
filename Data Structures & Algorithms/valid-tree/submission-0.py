class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        edge_ = defaultdict(list)

        for fn,sn in edges:
            edge_[fn].append(sn)
            edge_[sn].append(fn)

        bus = deque([0])      
        visited = set([0])

        while bus:
            current = bus.popleft()
            
            for neighbor in edge_[current]:
                if neighbor not in visited:
                    bus.append(neighbor)
                    visited.add(neighbor)


        return len(visited) == n