"""Graph drills.

Graphs are adjacency maps: ``{node: [neighbour, ...]}``. Weighted graphs use
``{node: [(neighbour, weight), ...]}``.
"""

from collections.abc import Mapping, Sequence

Graph = Mapping[str, Sequence[str]]
WeightedGraph = Mapping[str, Sequence[tuple[str, int]]]


def bfs_order(graph: Graph, start: str) -> list[str]:
    """Return nodes in breadth-first order from ``start``.

    Neighbours are visited in adjacency-list order. Target: O(V + E).
    """
    raise NotImplementedError


def dfs_order(graph: Graph, start: str) -> list[str]:
    """Return nodes in depth-first pre-order from ``start``.

    Neighbours are visited in adjacency-list order. Target: O(V + E).
    """
    raise NotImplementedError


def shortest_path(graph: Graph, start: str, end: str) -> list[str] | None:
    """Return the shortest unweighted path from ``start`` to ``end``.

    Return ``None`` if unreachable. Target: BFS with a parent map.
    """
    raise NotImplementedError


def has_path(graph: Graph, start: str, end: str) -> bool:
    """Return ``True`` if ``end`` is reachable from ``start``."""
    raise NotImplementedError


def detect_cycle_directed(graph: Graph) -> bool:
    """Return ``True`` if the directed graph contains a cycle.

    Target: DFS with a three-colour (white/grey/black) marking.
    """
    raise NotImplementedError


def topological_sort(graph: Graph) -> list[str] | None:
    """Return a topological ordering, or ``None`` if the graph has a cycle.

    Target: Kahn's algorithm, O(V + E).
    """
    raise NotImplementedError


def dijkstra(graph: WeightedGraph, start: str) -> dict[str, int]:
    """Return the shortest distance from ``start`` to every reachable node.

    Unreachable nodes are omitted. Weights are non-negative.
    Target: O((V + E) log V) with ``heapq``.
    """
    raise NotImplementedError


def num_islands(grid: Sequence[Sequence[str]]) -> int:
    """Count connected groups of ``"1"`` cells in a grid of ``"1"``/``"0"``.

    Cells connect 4-directionally. Target: O(rows * cols) flood fill.
    """
    raise NotImplementedError
