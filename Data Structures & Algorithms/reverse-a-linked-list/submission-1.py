# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''

        input = 0   1   2   3
               c   p

            given head
                curr
                next

        output= 3   2   1   0

        curr = head
        prev = None


        loop through linkedlist

            temp = curr.next  
            curr.next = prev
            prev = curr


            curr = temp



            
        '''

        curr = head
        prev = None

        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr

            curr = nxt

        return prev




        