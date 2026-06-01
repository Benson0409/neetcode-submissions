class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        parent = []
        boss = set()

        for i in range(n):
            parent.append(i)

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            
            return parent[i]

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            
            parent[root_a] = root_b

        for i in range(len(parent)):
            boss.add(find(i))

        return len(boss)

        


        
        