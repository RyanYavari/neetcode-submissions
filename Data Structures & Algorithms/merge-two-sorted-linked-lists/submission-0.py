# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Input: list1 = [1,2,4], list2 = [1,3,5]
        Output: [1,1,2,3,4,5]

        edge cases: 
        1. list1 = null, return list2
        2. list2 = null, return list2
                    

        if list1:
        dummy = node = ListNode()
        output = dummy

        if list1 is null and list2 exists, return list2
        if list2 is null and list1 exists, return list1

        # at this point, both lists exists



        while both lists are populated:
            if list1 is less than list2:
                output.next = list1
                list1 = list1.next
            elif list2 < list1:
                output.next = list2
                list2 = list2.next
        
        # if one of the lists are null

        if list1 is null and list2 exists
            output.next = list2
        elif list2 is null and list1 exists
            output.next = list1

        return dummy.next
        '''

        dummy = output = ListNode()
        

        # check if either list is null and other is populated
        if list1 and list2 == None:
            return list1
        elif list2 and list1 == None:
            return list2
        
        # at this point, both lists are populated
        while list1 and list2:
            
            #find smaller head
            
            #if list1 head is equal or smaller than list2 head, add head to output and increment head of list1
            if list1.val <= list2.val:
                output.next = list1
                list1 = list1.next
            
            # if list2 head is smaller than list1 head, add head to output and increment head of list2
            elif list2.val < list1.val:
                output.next = list2
                list2 = list2.next
            output = output.next
        
        # if one list becomes null
        if list1 and list2 == None:
            output.next = list1
        elif list2 and list1 == None:
            output.next = list2
        
        # at this point, output is fully populated. return next node after dummy node

        return dummy.next


        '''
        list1:  1   2   4
                            h
        
        list2:  1   3   5
                        h
        output = dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 5




        '''



        