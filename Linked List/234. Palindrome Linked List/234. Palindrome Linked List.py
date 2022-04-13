# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

def reverse(current,prev):
    if current == None:
        return prev
    next_node = current.next
    current.next = prev
    return reverse(next_node,current)
    
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next == None:
            return True
        s,f,prev = head,head,None
        while f and f.next:
            prev=s
            s= s.next
            f= f.next.next
            
        prev.next=None
        head1 = head
        head2 = s if f==None else s.next
        head2 = reverse(head2,None)
        while head2 and head1:
            if head1.val!=head2.val:
                return False
            head1=head1.next
            head2=head2.next
        return True


#This second solution would require extra memory since we're converting the list to an array
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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