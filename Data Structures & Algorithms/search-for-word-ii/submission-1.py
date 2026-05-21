
class TrieNode:
    def __init__(self):
        self.node = defaultdict(TrieNode)
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            current_node = root
            for char in word:
                current_node = current_node.node[char]
            current_node.word = word

        answer = []
        rows = len(board)
        cols = len(board[0])


        def dfs(r, c, current_node):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == "#":
                return
            
            char = board[r][c]
            
            if char not in current_node.node:
                return
            
            next_node = current_node.node[char]
            
            if next_node.word != None:
                answer.append(next_node.word)
                next_node.word = None 

            board[r][c] = "#"
            
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)
            
            board[r][c] = char
            
            if not next_node.node:
                del current_node.node[char]

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)

        return answer


        