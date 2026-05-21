class WordDictionary:

    def __init__(self):
        self.node = defaultdict(WordDictionary)
        self.isEnd = False

    def addWord(self, word: str) -> None:
        current_node = self

        for i in word:
            current_node = current_node.node[i]
        current_node.isEnd = True

    def search(self, word: str) -> bool:

        current_node = self

        def dfs(node,char) -> bool:
            if len(char) == 0:
                return node.isEnd

            first_c = char[0]
            other_c = char[1:]

            if first_c == ".":
                for next_node in node.node.values():
                    if dfs(next_node, other_c) == True:
                        return True
                return False
            else:
                if first_c not in node.node:
                    return False
                node = node.node[first_c]
                return dfs(node,other_c)
        
        return dfs(current_node,word)
             
        
