class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        return less + equal + greater
Example
nums = [9,12,5,10,14,3,10]
pivot = 10
sol = Solution()
print(sol.pivotArray(nums, pivot))



Output:
[9, 5, 3, 10, 10, 12, 14]



Complexity:
Time: O(n)
Space: O(n)
