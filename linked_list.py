class LinkedList:
    def __init__(self, nodes):
        self.head = nodes[0]

        i = 0
        while i <= len(nodes) - 2:
            nodes[i].next = nodes[i + 1]
            i += 1

        nodes[len(nodes) - 1].next = None


class Node:
    def __init__(self, value):
        self.value = value


nodes = [Node(0), Node(1), Node(2), Node(2)]
linked_list = LinkedList(nodes)

current_node = linked_list.head

while current_node.next is not None:
    print(current_node)
    current_node = current_node.next
