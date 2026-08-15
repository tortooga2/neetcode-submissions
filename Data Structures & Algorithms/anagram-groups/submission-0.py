class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for s in strs:
            found = False
            for o in output:
                if len(s) != len(o[0]):
                    continue
                l_dict = {}
                s_dict = {}

                for i in s:
                    if i in s_dict:
                        s_dict[i] += 1
                    else:
                        s_dict[i] = 1
                
                for j in o[0]:
                    if j in l_dict:
                        l_dict[j] += 1
                    else:
                        l_dict[j] = 1
                
                if l_dict == s_dict:
                    found = True
                    o.append(s)
                    break
            if not found:
                output.append([s])
        return output