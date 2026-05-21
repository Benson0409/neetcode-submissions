class PrefixTree:

    def __init__(self):
        self.node = defaultdict(PrefixTree)
        self.isEnd = False

    def insert(self, word: str) -> None:
        current_node = self
        for i in word:
            current_node = current_node.node[i]

        current_node.isEnd = True

    def search(self, word: str) -> bool:
        current_node = self
        for i in word:

            if i not in current_node.node:
                return False
            
            current_node = current_node.node[i]
        return current_node.isEnd
            

    def startsWith(self, prefix: str) -> bool:
        current_node = self
        
        for i in prefix:

            if i not in current_node.node:
                return False
            current_node = current_node.node[i]

        return True
        