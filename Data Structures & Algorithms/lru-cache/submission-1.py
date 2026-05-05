class LRUCache:

    def __init__(self, capacity: int):
        self.cach = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cach:
            ans = self.cach.pop(key)
            self.cach[key] = ans
            return ans

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cach:
            self.cach.pop(key)
        elif len(self.cach) >= self.capacity:
            oldest_key = next(iter(self.cach))
            self.cach.pop(oldest_key)

        self.cach[key] = value
