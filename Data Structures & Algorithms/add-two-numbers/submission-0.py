# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''

        1 <= n <= 


        Input: l1 and l2
        each list represents a integer >= 0
            integers stored in reverse order

            integer 321 : 1-> 2-> 3-> 
                digits stored in reverse order

        
        input [1, 2, 3] -> represents 321
              [4, 5, 6] -> represents 654

        output (321 + 654 = 975) : 5 -> 7 -> 9

        constraints:
        0 <= node.val <= 9
        1 <= length <= 100

        implementation:

        1. reverse l1 and calculate integer from l1

        2. reverse l2 and calculate int from l2

        3. calculate sum of both ints from l1 + l2

        4. create a linked list

        5. return the reversed linked list

        '''

        l1_val = ""
        l2_val = ""
        output_val = ""
        dummy = output = ListNode()

        # reverse l1 

        curr = l1
        prev = None
        while curr:
            #reversing the linked list
            nxt = curr.next
            curr.next = prev
            
            #setting up the next iteration
            prev = curr
            curr = nxt
        
        # prev is now the head of the reversed reverse linked list -> linked list 
        # [1, 2, 3] -> [3, 2, 1]
        
        #calculate integer from l1
        while prev:
            l1_val += str(prev.val)
            prev = prev.next
        
        l1_val = int(l1_val)

        # reverse l2 

        curr = l2
        prev = None
        while curr:
            #reversing the linked list
            nxt = curr.next
            curr.next = prev
            
            #setting up the next iteration
            prev = curr
            curr = nxt
        
        # prev is now the head of the reversed reverse linked list -> linked list 
        # [1, 2, 3] -> [3, 2, 1]
        
        #calculate integer from l1
        while prev:
            l2_val += str(prev.val)
            prev = prev.next
        
        l2_val = int(l2_val)

        sumNums = l1_val + l2_val

        sumNums = str(sumNums)


        #4. create a linked list of nodes of characters from a string

        '''
        for c in string:
            create a node for string 
            append node to end of linkedlist



        '''

        curr = output

        for c in sumNums:
            node = ListNode()
            node.val = int(c)
            output.next = node
            output = output.next




        #5. return the reversed linked list

        curr = dummy.next
        prev = None
        while curr:
            #reversing the linked list
            nxt = curr.next
            curr.next = prev
            
            #setting up the next iteration
            prev = curr
            curr = nxt
        
        return output
        







        