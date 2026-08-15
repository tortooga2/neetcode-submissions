class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            t = 0
            higher_temp_found = False
            for i2 in range(i, len(temperatures)):
                if temperatures[i2] > temperatures[i]:
                    higher_temp_found = True
                    break
                else:
                    t+=1
            if higher_temp_found:
                output.append(t)
            else:
                output.append(0)
        return output

        