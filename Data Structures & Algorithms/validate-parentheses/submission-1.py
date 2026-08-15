class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in s:
            if i == '(' or i == "[" or i == '{':
                queue.append(i)
            else:
                if not queue:
                    return False
                if i == ')' and queue[-1] == '(':
                    queue = queue[:-1]
                elif i==']' and queue[-1] == '[':
                    queue = queue[:-1]
                elif i=='}' and queue[-1] == '{':
                    queue = queue[:-1]
                else:
                    return False
        if len(queue) != 0:
            return False
        return True
