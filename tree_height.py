class Tree:
    def __init__(self, n, nodes):
        """
        :param n: number of nodes
        :param nodes: list of nodes. index i is node key, value at index i is parent node
        """
        assert len(nodes) == n, f'`nodes` should contain exactly {n} elements'

        for i in range(n):
            node = Node(i)
            parent = nodes[i]

            if parent == -1:
                self.root = node
                continue

            node.parent = Node(parent)


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None


n = 4
nodes = [4, -1, 4, 1, 1]

tree = Tree(n, nodes)
print(tree.root.key)

