class Solution:
    def constructList(self, queries):
        # code here
        xor_val = 0
        arr = [0]

        for typ, x in queries:
            if typ == 0:
                arr.append(x ^ xor_val)
            else:
                xor_val ^= x

        for i in range(len(arr)):
            arr[i] ^= xor_val

        arr.sort()
        return arr
