class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        window = {}

        for R in range(len(s2)):
            window[s2[R]] = 1 + window.get(s2[R], 0)
            window_len = R - L + 1


            
            while window_len > len(s1):
                window[s2[L]] -= 1
                if window[s2[L]] == 0:
                    del window[s2[L]]
                L += 1
                window_len = R - L + 1

            temp = {}
            for i in s1:
                temp[i] = 1 + temp.get(i, 0)
            
            if temp == window:
                return True

            
                
            
            
        return False
            
        