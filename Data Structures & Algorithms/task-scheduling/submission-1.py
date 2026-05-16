class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        data = {}
        for i in tasks:
            data[i] = data.get(i, 0) + 1
            
        max_time = max(data.values()) # 找出最大次數
        
        # 修正這裡：把 values 轉成 list，然後用 .count() 去數 max_time 出現幾次
        counts_list = list(data.values())
        num_of_count = counts_list.count(max_time) 

        current = (max_time - 1) * (n + 1) + num_of_count

        return max(current, len(tasks))