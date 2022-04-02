# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNoteBook]) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True