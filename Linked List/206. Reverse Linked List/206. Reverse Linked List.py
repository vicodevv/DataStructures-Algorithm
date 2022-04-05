# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNoteBook]:
        prev, curr = None, head
        
        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev