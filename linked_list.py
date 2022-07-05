class LinkedList:
    def __init__(self, nodes):
        self.head = nodes[0]
        self.tail = nodes[-1]

        i = 0
        while i <= len(nodes) - 2:
            nodes[i].next = nodes[i + 1]
            nodes[i].tail = None
            i += 1

        nodes[len(nodes) - 1].next = None
        nodes[len(nodes) - 1].tail = True


class Node:
    def __init__(self, value):
        self.value = value


nodes = [Node(0), Node(1), Node(2), Node(2)]
linked_list = LinkedList(nodes)

current_node = linked_list.head

while current_node.next is not None:
    print(current_node)
    current_node = current_node.next
