class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c

i = a
while i:
    print(i.data)
    i = i.next
