class TimeMap:

    def __init__(self):
        self.m = {}
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = [(timestamp, value)]
        else:
            vals = self.m[key]
            vals.append((timestamp, value))
            self.m[key] = sorted(vals)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        vals = self.m[key]

        l, r = 0, len(vals) - 1
        while l < r:
            m = l + (r - l) // 2 + 1
            if timestamp >= vals[m][0]:
                l = m
            else:
                r = m - 1
        
        if timestamp < vals[l][0]:
            return ""
        return vals[l][1]

        
        
        
        

        
                
        
                

