"""
Remove Linked List Elements
描述
Remove all elements from a linked list of integers that have value val.

说明
样例
Example 1:

Input: head = 1->2->3->3->4->5->3->null, val = 3
Output: 1->2->4->5->null
Example 2:

Input: head = 1->1->null, val = 1
Output: null

Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here