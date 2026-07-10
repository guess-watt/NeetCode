# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(0)
        # curr = dummy

        # while list1 and list2:
        #     if list1.val <= list2.val:
        #         curr.next = list1
        #         list1 = list1.next
        #     else:
        #         curr.next = list2
        #         list2 = list2.next

        #     curr = curr.next
        
        # curr.next = list1 or list2

        # return dummy.next
        # it is working


        dummy = ListNode()
        curr = dummy
        result = []
        while list1:
            result.append(list1.val)
            list1 = list1.next
        
        while list2:
            result.append(list2.val)
            list2 = list2.next
            
        result.sort()

        for i in result:
            curr.next = ListNode(i)
            curr = curr.next
        
        
        return dummy.next