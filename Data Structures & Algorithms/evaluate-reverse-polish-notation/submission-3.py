class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t not in ['+', '*', '/', '-']:
                st.append(int(t))
            else:
                b = st.pop()
                a = st.pop()
                if t == '+':
                    s = a + b
                elif t == '*':
                    s = a * b
                elif t == '/':
                    s = int(a / b)
                elif t == '-':
                    s = a - b
                st.append(s)
        return int(st[0])