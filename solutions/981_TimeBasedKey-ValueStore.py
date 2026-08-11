class TimeMap:

    def __init__(self):
        self.log = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.log:
            self.log[key].append([value, timestamp])

        else:
            self.log[key] = [[value, timestamp]]

        # print(f"added: {key}, log: {self.log}")

    def getBS(self, vals, timestamp):
        last_val = ""
        start = 0 
        end = len(vals) - 1

        while start <= end:
            mid = start + ((end - start) // 2)

            if vals[mid][1] <= timestamp:
                last_val = vals[mid][0]
                start = mid + 1

            else:
                end = mid - 1

        return last_val

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.log:
            return ""
        
        return self.getBS(self.log[key], timestamp)

        

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))        
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))         
print(timeMap.get("foo", 5))      
