class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return True
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        s = list(s)
        print(s)
        p1 = 0
        p2 = len(s) - 1
        
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True



        