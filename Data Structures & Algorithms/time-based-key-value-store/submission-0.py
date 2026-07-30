class TimeMap:

    def __init__(self):
        self.key_store = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return ""

        enteries = self.key_store[key]
        lp = 0
        rp = len(enteries) - 1
        result = ""

        while lp <= rp:
            mid_index = (lp + rp) // 2
            mid_timestamp, mid_val = enteries[mid_index]

            if mid_timestamp <= timestamp:
                result = mid_val
                lp = mid_index + 1
            else:
                rp = mid_index - 1

        return result 
        
