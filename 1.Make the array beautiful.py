class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        stack = []
        for i in arr:
            if stack and ((stack[-1] >= 0 and i < 0) or (stack[-1] < 0 and i >= 0)):
                stack.pop()
            else:
                stack.append(i)
        return stack
