class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
            
        bus = deque([(beginWord, 1)])
        
        while bus:
            current_word, steps = bus.popleft()
            
            if current_word == endWord:
                return steps
                
            for i in range(len(current_word)):
                for char_code in range(97, 123): 
                    new_char = chr(char_code)
                    if new_char == current_word[i]:
                        continue
                        
                    new_word = current_word[:i] + new_char + current_word[i+1:]
                    
                    if new_word in word_set:
                        bus.append((new_word, steps + 1))
                        word_set.remove(new_word)
                        
        return 0