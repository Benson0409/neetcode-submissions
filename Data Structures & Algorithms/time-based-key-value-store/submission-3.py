class TimeMap:

    def __init__(self):
        
        self.timestamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        data = (timestamp,value)

        if key in self.timestamp:
            self.timestamp[key].append(data)
        else:
            self.timestamp[key] = []
            
            self.timestamp[key].append(data)

    def get(self, key: str, timestamp: int) -> str:

        if key not in  self.timestamp:
            return ""
        data = self.timestamp[key]
        left = 0
        right = len(data)-1

        while left <= right:
            mid = (left+right) // 2

            if data[mid][0] == timestamp:
                return data[mid][1]
            elif data[mid][0] > timestamp:
                right = mid -1
            elif data[mid][0] < timestamp:
                left = mid + 1

        if right < 0:
            return""
        return data[right][1]
