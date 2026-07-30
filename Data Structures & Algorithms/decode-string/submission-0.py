class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        result = []
        for char in s:
            if char == "]":
                values = []
                while stack[-1] != "[":
                    values.append(stack.pop())
                values.reverse()
                stack.pop()
                digit = []
                while stack and stack[-1].isdigit():
                    digit.append(stack.pop())
                digit.reverse()
                digit = ''.join(digit)
                stack.append(int(digit) * ''.join(values))
            else:
                stack.append(char)

        return ''.join(stack)

        