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
        if node in list(self.graph.keys()):
            raise KeyError("Node already in graph.")
        self.graph[node] = {}

    def add_edge(self, node1, node2, weight=0):
        """Add an edge from node1 to node2 in the graph."""
        if node1 not in list(self.graph.keys()):
            self.add_node(node1)
        if node2 not in list(self.graph.keys()):
            self.add_node(node2)
        if node2 not in list(self.graph[node1].keys()):
            self.graph[node1][node2] = weight

    def nodes(self):
        """Return a list of all nodes in the graph."""
        node_list = []
        for node in list(self.graph.keys()):
            node_list.append(node)
        return node_list

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for node in list(self.graph.keys()):
            edge_list.append("{}: {}".format(node, list(self.graph[node].keys())))
        return edge_list

    def del_node(self, node):
        """Delete node n from the graph, raises error if does not exist."""
        if node not in list(self.graph.keys()):
            raise KeyError("You can't delete a node that does not exist.")
        del self.graph[node]
        for key in list(self.graph.keys()):
            if node in list(self.graph[key].keys()):
                del self.graph[key][node]

    def del_edge(self, node1, node2):
        """Delete the edge connecting n1 and n2."""
        if node2 in list(self.graph[node1].keys()) and self.graph[node2]:
            del self.graph[node1][node2]
        elif node1 not in list(self.graph.keys()) or node2 not in list(self.graph.keys()):
            raise KeyError("That node is not in the graph.")
        else:
            raise ValueError("That edge is not in the graph.")

    def has_node(self, node):
        """Return True if node n is contained in the graph."""
        return node in list(self.graph.keys())

    def neighbors(self, node):
        """Return a list of all nodes connected to n by edges."""
        if node not in list(self.graph.keys()):
            raise KeyError("Not in graph.")
        return self.graph[node]

    def adjacent(self, node1, node2):
        """Return True if n1 and n2 are connected by an edge."""
        if node1 not in list(self.graph.keys()):
            raise KeyError("{} is not in the graph.".format(node1))
        elif node2 not in list(self.graph.keys()):
            raise KeyError("{} is not in the graph.".format(node2))
        return node1 in list(self.graph[node2].keys()) or node2 in list(self.graph[node1].keys())

    def depth_traversal(self, start, checked=None):
        """Traverse the graph by depth."""
        if start not in list(self.graph.keys()):
            raise KeyError("{} not in graph.".format(start))
        if checked is None:
            checked = []
        checked.extend([start])
        for edge in list(self.graph[start].keys()):
            if edge not in checked:
                self.depth_traversal(edge, checked)
        return checked

    def breadth_traversal(self, start):
        """Traverse the graph by breadth."""
        checked, node_list = [], [start]
        while node_list:
            vertex = node_list.pop(0)
            if vertex not in checked:
                checked.append(vertex)
                [node_list.append(edge) for edge in list(self.graph[vertex].keys())
                    if edge not in checked]
        return checked

    def heuristic(self, start):
        """Run BFS to set a heuristic for A* algorithm on a simple weighted graph."""
        node_list = [start]
        checked, weights = [], []
        while node_list:
            vertex = node_list.pop(0)
            if vertex not in checked:
                checked.append(vertex)
                for key, weight in self.graph[vertex].items():
                    if self.graph[vertex][key] not in checked:
                        weights.append(weight)
                        node_list.append(key)
        print("weights: " + str(weights))
        print("sum of weights: " + str(sum(weights)))
        print("node_list: " + str(node_list))
        print("checked: " + str(checked))
        return sum(weights) / len(checked)

    def a_star_search(self, start, goal):
        """Do an A* search."""
        from priority_queue import Priority_Q
        avg_weight = self.heuristic(start)
        print(avg_weight)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        a_star_priorityq = Priority_Q()
        a_star_priorityq.insert(start, 0)
        print(type(a_star_priorityq))
        print(a_star_priorityq.peek())
        while self.neighbors(a_star_priorityq.peek()[0]):
            try:
                current = a_star_priorityq.pop()

                if current == goal:
                    break

                for next in self.neighbors(current[0]):
                    new_cost = cost_so_far[current] + self.graph[current][next]
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        priority = new_cost + avg_weight
                        a_star_priorityq.insert(next, priority)
                        came_from[next] = current
            except IndexError:
                print("IndexError: you can't get there from here.")

        return came_from, cost_so_far

    def reconstruct_path(came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.append(start) # optional
        path.reverse() # optional
        return path

    def dijkstra(self, start, finish):
        """Return the shortest path between two nodes.
        Return the path and the number of steps taken to follow that path."""

        unvisited = self.depth_traversal(start)
        distances = {i: [None, [None]] for i in unvisited}
        distances[start] = [0, [start]]
        current_node = start

        if start not in unvisited:
            raise KeyError("The start node is not in the graph.")
        elif finish not in unvisited:
            raise ValueError("The finish node is not in the graph.")

        while unvisited:
            for item in self.neighbors(current_node):
                study_node = item
                current_node_distance = distances[current_node][0]
                potential_distance = self.neighbors(current_node)[study_node]
                original_distance = distances[study_node][0]

                if study_node not in unvisited:
                    continue
                elif original_distance is None or potential_distance < original_distance:
                    current_node_path = (distances[current_node])[1][:]
                    current_node_path.append(study_node)
                    distances[study_node][0] = potential_distance + current_node_distance
                    distances[study_node][1] = current_node_path
                    continue

            if current_node == finish:
                return distances[finish]

            unvisited.remove(current_node)
            next_node = None
            for key, value in distances.items():
                if key in unvisited:
                    if next_node is None:
                        next_node = key
                        continue
                    elif distances[key][0]:
                        if distances[key][0] < distances[next_node][0]:
                            next_node = key
            current_node = next_node

dummy = Graph()
dummy.add_edge(1, 2, 2)
dummy.add_edge(1, 3, 1)
dummy.add_edge(2, 4, 4)
dummy.add_edge(3, 5, 3)
dummy.add_edge(4, 6, 6)
dummy.add_edge(5, 6, 5)

dummy.dijkstra(1, 6)



# if __name__ == "__main__":
#     """Calculate the runtime for depth_traversal and breadth_traversal."""
#     import timeit



#     depth = timeit.timeit(
#         stmt="dummy.depth_traversal(1)",
#         setup="from __main__ import dummy",
#         number=1000
#     )
#     breadth = timeit.timeit(
#         stmt="dummy.breadth_traversal(1)",
#         setup="from __main__ import dummy",
#         number=1000
#     )
#     print("It takes {} ms to run depth_traversal, and {} ms to run breadth_traversal".format(depth, breadth))
