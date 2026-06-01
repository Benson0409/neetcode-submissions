class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        parent = []
        count = n

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
            
            if root_a != root_b:
                parent[root_a] = root_b
                count -= 1

        return count

        


        
        