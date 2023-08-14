"""
https://py.checkio.org/en/mission/count-chains/


In this mission you must count chains.

You are given a list of details of the circle (tuple of X-coordinate, Y-coordinate, radius).
You have to return the number of groups of circles where their circumferences intersect.

NOTE:

Only one circle counts as one group.

Example:

count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2
count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1
count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4

"""
from math import sqrt
from typing import NamedTuple, TypeAlias

CircleInput: TypeAlias = tuple[int, int, int]


class Circle(NamedTuple):
    x: int
    y: int
    radius: int


class CircleGroups:
    def __init__(self, circles: list[Circle]):
        self.circles: list[Circle] = circles
        self.circles_count: int = len(circles)
        self.graph = self._build_graph()
        print(self.graph)
        self.visited: list[bool] = [False] * len(circles)
        self.chains: int = self.count_chains()

    @staticmethod
    def circles_intersect(c1: Circle, c2: Circle) -> bool:
        """
        Determines if two circles intersect.

        Returns:
        - bool: True if circles intersect, False otherwise
        """
        distance = sqrt((c2.x - c1.x) ** 2 + (c2.y - c1.y) ** 2)

        # Ensure one circle is not entirely inside the other
        if abs(c1.radius - c2.radius) < distance:
            return distance < c1.radius + c2.radius
        return False

    def _build_graph(self) -> list[list[int]]:
        """
        Builds a graph where each node represents a circle and an edge between two nodes indicates
        that the corresponding circles intersect.

        Returns:
        - List[List[int]]: Adjacency list representation of the graph
        """
        graph = [[] for _ in range(self.circles_count)]
        for i in range(self.circles_count):
            for j in range(i + 1, self.circles_count):
                if self.circles_intersect(self.circles[i], self.circles[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        return graph

    def _dfs(self, node: int) -> None:
        """
        Depth-First Search to explore the graph.

        Args:
        - node: Current node being explored

        Returns:
        - None
        """
        self.visited[node] = True
        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                self._dfs(neighbor)

    def count_chains(self) -> int:
        """
        Counts the number of groups of circles where their circumferences intersect.

        Returns:
        - int: Number of groups
        """
        components = 0
        for i in range(len(self.circles)):
            if not self.visited[i]:
                self._dfs(i)
                components += 1
        return components


def count_chains(circles: list[CircleInput]) -> int:
    """
    Counts the number of groups of circles where their circumferences intersect.

    Args:
    - circles: List of tuples representing circles (x, y, radius)

    Returns:
    - int: Number of groups
    """
    circles = [Circle(*circle) for circle in circles]
    return CircleGroups(circles).chains
