class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            min_num = val
        else:
            min_num = min(self.stack[-1][-1],val)
        self.stack.append((val,min_num))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]       
