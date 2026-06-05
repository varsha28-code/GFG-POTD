class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0

    def lexicographicallySmallest(self, s, k):
        n = len(s)

        # Correct k
        if self.isPowerOfTwo(n):
            k //= 2
        else:
            k *= 2

        # Not possible or empty result
        if k >= n:
            return "-1"

        stack = []
        remove = k

        for ch in s:
            while stack and remove > 0 and stack[-1] > ch:
                stack.pop()
                remove -= 1
            stack.append(ch)

        # Remove remaining characters from the end
        while remove > 0:
            stack.pop()
            remove -= 1

        result = ''.join(stack)
        return result if result else "-1"


# Driver Code
s = input().strip()
k = int(input())

obj = Solution()
print(obj.lexicographicallySmallest(s, k))
