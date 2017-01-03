"""Create an unweighted, directed graph."""


class Graph():
    """
    Create an unweighted, directed graph instance with the following methods.

    nodes(): returns a list of all nodes in the graph.

    edges(): returns a list of all edges in the graph.

    add_node(n): adds a new node, n, to the graph.

    add_edge(n1, n2): adds n1 and n2 if they don't exist, and adds an edge connecting them.

    del_node(n): deletes node n from the graph.

    del_edge(n1, n2): deletes the edge connecting n1 and n2.

    has_node(n): Returns True if node n is contained in the graph.

    neighbors(n): Returns a list of all nodes connected to n by edges.

    adjacent(n1, n2): returns True if n1 and n2 are connceted by an edge.
    """

    def __init__(self):
        """Instantiate a new graph instance."""
        self.graph = {}

    def add_node(self, node):
        """Add a node to the graph."""
        if node in self.graph.keys():
            raise KeyError("Node already in graph.")
        self.graph[node] = {"edge_and_weight": []}

    def add_edge(self, node1, node2, weight=0):
        """Add an edge from node1 to node2 in the graph."""
        if node1 not in self.graph.keys():
            self.add_node(node1)
        if node2 not in self.graph.keys():
            self.add_node(node2)
        if node2 not in self.graph[node1]['edge_and_weight']:
            self.graph[node1]['edge_and_weight'].append((node2, weight))

    def nodes(self):
        """Return a list of all nodes in the graph."""
        node_list = []
        for node in self.graph.keys():
            node_list.append(node)
        return node_list

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for node in self.graph.keys():
            edge_list.append("{}: {}".format(node, self.graph[node]["edge_and_weight"]))
        return edge_list

    def del_node(self, node):
        """Delete node n from the graph, raises error if does not exist."""
        if node not in self.graph.keys():
            raise KeyError("You can't delete a node that does not exist.")
        del self.graph[node]
        for key in self.graph.keys():
            if node in self.graph[key]["edge_and_weight"]:
                self.graph[key]["edge_and_weight"].remove(node)

    def del_edge(self, node1, node2):
        """Delete the edge connecting n1 and n2."""
        if self.graph[node1]['edge_and_weight'] and self.graph[node2]:
            self.graph[node1]['edge_and_weight'].remove(node2)
        elif node1 not in self.graph.keys() or node2 not in self.graph.keys():
            raise KeyError("That node is not in the graph.")
        else:
            raise ValueError("That edge is not in the graph.")

    def has_node(self, node):
        """Return True if node n is contained in the graph."""
        return node in self.graph.keys()

    def neighbors(self, node):
        """Return a list of all nodes connected to n by edges."""
        if node not in self.graph.keys():
            raise KeyError("Not in graph.")
        return self.graph[node]['edge_and_weight']

    def adjacent(self, node1, node2):
        """Return True if n1 and n2 are connected by an edge."""
        if node1 not in self.graph.keys():
            raise KeyError("{} is not in the graph.".format(node1))
        elif node2 not in self.graph.keys():
            raise KeyError("{} is not in the graph.".format(node2))
        return node1 in self.graph[node2]['edge_and_weight'] or node2 in self.graph[node1]['edge_and_weight']

    def depth_traversal(self, start, checked=None):
        """Traverse the graph by depth."""
        if start not in list(self.graph):
            raise KeyError("{} not in graph.".format(start))
        if checked is None:
            checked = []
        checked.extend([start])
        for edge in self.graph[start]["edge_and_weight"]:
            if edge[0] not in checked:
                self.depth_traversal(edge[0], checked)
        return checked

    def breadth_traversal(self, start):
        """Traverse the graph by breadth."""
        checked, node_list = [], [start]
        while node_list:
            vertex = node_list.pop(0)
            if vertex not in checked:
                checked.append(vertex)
                [node_list.append(edge[0]) for edge in self.graph[vertex]['edge_and_weight']
                    if edge[0] not in checked]
        return checked


if __name__ == "__main__":
    """Calculate the runtime for depth_traversal and breadth_traversal."""
    import timeit

    dummy = Graph()
    dummy.add_edge(1, 2)
    dummy.add_edge(1, 3)
    dummy.add_edge(1, 7)
    dummy.add_edge(2, 3)
    dummy.add_edge(2, 4)
    dummy.add_edge(7, 5)
    dummy.add_edge(7, 10)

    depth = timeit.timeit(
        stmt="dummy.depth_traversal(1)",
        setup="from __main__ import dummy",
        number=1000
    )
    breadth = timeit.timeit(
        stmt="dummy.breadth_traversal(1)",
        setup="from __main__ import dummy",
        number=1000
    )
    print("It takes {} ms to run depth_traversal, and {} ms to run breadth_traversal".format(depth, breadth))
