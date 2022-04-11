# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNoteBook], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev, curr = dummy, head
        
        while curr:
            nxt = curr.next
        
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            
            curr = nxt
            
        return dummy.next