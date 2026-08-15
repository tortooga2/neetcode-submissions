class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_list = list(t)
        s_list = list(s)
        
        t_list.sort()
        s_list.sort()

        return all(t_list[i] == s_list[i] for i in range(len(t_list)))