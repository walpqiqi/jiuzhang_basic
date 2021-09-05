class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, location):
        pre = self.head
        for i in range(location):
            pre = pre.next

        return pre.value

    def add(self, location, val):
        if location > 0:
            pre = self.head

            for i in range(location-1):
                pre = pre.next

            new_node = ListNode(val)
            new_node.next = pre.next
            pre.next = new_node
        elif location ==0:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node

    def set(self, location, val):
        cur = self.head
        for i in range(location):
            cur = cur.next
        cur.val = val

    def remove(self, location):
        if location ==0:
            self.head = self.head.next
        elif location > 0:
            pre = self.head
            for i in range(location -1):
                pre = pre.next
            pre.next = pre.next.next

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.val , end='')
            cur = cur.next
        print()

    def is_empty(self):
        return self.head is None