class Solution:
    def compute(self, head):
        # Reverse linked list
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head = prev

        # Delete nodes smaller than max seen so far
        max_val = head.data
        curr = head

        while curr and curr.next:
            if curr.next.data < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.data

        # Reverse again
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev





A space-efficient approach is:

->Reverse the linked list.
->Traverse from left to right (which is originally right to left).
->Keep track of the maximum value seen so far.
->Delete nodes whose value is less than the maximum.
->Reverse the list again.




Example

Input:

12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3

After first reverse:

3 -> 2 -> 6 -> 5 -> 11 -> 10 -> 15 -> 12

Removing nodes smaller than maximum seen:

3 -> 6 -> 11 -> 15

Reverse again:

15 -> 11 -> 6 -> 3

Output:

15 -> 11 -> 6 -> 3

Complexity:

Time: O(n)
Auxiliary Space: O(1)
This works in O(n) time and O(1) extra space.







