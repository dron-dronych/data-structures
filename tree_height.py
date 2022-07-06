class Tree:
    def __init__(self, n, nodes):
        """
        :param n: number of nodes
        :param nodes: list of nodes. index i is node key, value at index i is parent node
        """
        assert len(nodes) == n, f'`nodes` should contain exactly {n} elements'

        nodes_list = []

        for i in range(n):
            node = Node(i)
            parent = nodes[i]

            if parent == -1:
                self.root = node
                nodes_list.append(node)
                continue

            node.parent = Node(parent)

            nodes_list.append(node)

        self.nodes = nodes_list

    def height(self):
        pass


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None

    def __repr__(self):
        return f'Node(key={self.key}, parent={self.parent})'





n = 5
nodes = [4, -1, 4, 1, 1]

tree = Tree(n, nodes)
print(tree.nodes)

