class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        parent = []

        for i in range(n):
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
                return False

            parent[root_a] = root_b
        return True