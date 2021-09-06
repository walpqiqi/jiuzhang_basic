"""
Reverse Linked List
描述
Reverse a linked list.

说明
样例
Example 1:

Input:

linked list = 1->2->3->null
Output:

3->2->1->null
Explanation:

Reverse Linked List

Example 2:

Input:

linked list = 1->2->3->4->null
Output:

4->3->2->1->null
Explanation:

Reverse Linked List

挑战
Reverse it in-place and in one-pass

Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here