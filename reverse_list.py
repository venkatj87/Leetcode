# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        newlist = None
        while current:
            next_node = current.next
            current.next = newlist
            newlist = current
            current = next_node
        return newlist
