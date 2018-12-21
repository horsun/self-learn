class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


link = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node())))))))


def nodeReverse(link):
    pre = link
    current = link.next
    pre.next = None
    while current:
        temp = current.next
        current.next = pre
        pre = current
        current = temp
    return pre


root = nodeReverse(link=link)
while root:
    print(root.data)
    root = root.next
