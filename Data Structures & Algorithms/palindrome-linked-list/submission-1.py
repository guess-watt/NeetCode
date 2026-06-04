# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = []
        while head:
            dummy.append(head.val)
            head = head.next
        if dummy == dummy[::-1]:#slicing better reverse() does not work bec it returns None
            return True
        else:return False
        


        