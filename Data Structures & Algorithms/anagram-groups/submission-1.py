class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = {}
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in output_dict:
                output_dict[sortedStr].append(s)
            else:
                output_dict[sortedStr] = [s]
        return list(output_dict.values())