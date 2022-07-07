class Tree:
    def __init__(self, n, nodes):
        """
        :param n: number of nodes
        :param nodes: list of nodes. index i is node key, value at index i is parent node
        """
        assert len(nodes) == n, f'`nodes` should contain exactly {n} elements'

        nodes_list = [Node(i) for i in range(n)]

        for i in range(n):
            parent = nodes[i]

            if parent == -1:
                self.root = nodes_list[i]

            else:
                nodes_list[parent].set_child(nodes_list[i])

        self.nodes = nodes_list

    def height(self):
        pass


class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

    def set_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f'Node(key={self.key}, children={self.children})'





n = 5
nodes = [4, -1, 4, 1, 1]

tree = Tree(n, nodes)
for node in tree.nodes:
    print(node)

print(f'root: {tree.root}')

