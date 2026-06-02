class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        count = len(edges)
        edge = []
        parent = []
        for i in range(count+1):
            parent.append(i)

        def find(i):
            if parent[i] == i:
                return i

            parent[i] = find(parent[i])
            return parent[i]

        for a,b in edges:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                edge = [a,b]

            parent[root_a] = root_b

        return edge