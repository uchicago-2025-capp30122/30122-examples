# data-structures/linked_list.py
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None

    def __len__(self):
        count = 0
        cur = self.root
        while cur is not None:
            count += 1
            cur = cur.next

    def append(self, value):
        # new tail node
        new = Node(value)
        # special case for first node
        if self.root is None:
            self.root = new
        else:
            cur = self.root
            # iterate to end-1
            while cur.next is not None:
                cur = cur.next
            # append node
            cur.next = new

    def prepend(self, value):
        # add new node that points at old root
        new = Node(value, self.root)
        self.root = new

    def __str__(self):
        s = ""
        cur = self.root
        while cur:
            s += f"{cur.value} -> "
            cur = cur.next
        s += "END"
        return s


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
ll.prepend(-1)
ll.append(3)
print(ll)
