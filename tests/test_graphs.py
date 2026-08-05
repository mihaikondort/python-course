import pytest

from interview_prep.algorithms.graphs import (
    bfs_order,
    detect_cycle_directed,
    dfs_order,
    dijkstra,
    has_path,
    num_islands,
    shortest_path,
    topological_sort,
)


@pytest.fixture
def graph():
    return {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D", "E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
        "Z": [],
    }


class TestTraversals:
    def test_bfs(self, graph):
        assert bfs_order(graph, "A") == ["A", "B", "C", "D", "E", "F"]

    def test_dfs(self, graph):
        assert dfs_order(graph, "A") == ["A", "B", "D", "F", "C", "E"]

    def test_isolated_node(self, graph):
        assert bfs_order(graph, "Z") == ["Z"]
        assert dfs_order(graph, "Z") == ["Z"]

    def test_handles_cycles(self):
        cyclic = {"A": ["B"], "B": ["A"]}
        assert bfs_order(cyclic, "A") == ["A", "B"]
        assert dfs_order(cyclic, "A") == ["A", "B"]


class TestPaths:
    def test_shortest_path(self, graph):
        assert shortest_path(graph, "A", "F") == ["A", "B", "D", "F"]

    def test_same_node(self, graph):
        assert shortest_path(graph, "A", "A") == ["A"]

    def test_unreachable(self, graph):
        assert shortest_path(graph, "A", "Z") is None

    def test_has_path(self, graph):
        assert has_path(graph, "A", "F") is True
        assert has_path(graph, "A", "Z") is False


class TestCycleAndTopo:
    def test_no_cycle(self, graph):
        assert detect_cycle_directed(graph) is False

    def test_cycle(self):
        assert detect_cycle_directed({"A": ["B"], "B": ["C"], "C": ["A"]}) is True

    def test_self_loop(self):
        assert detect_cycle_directed({"A": ["A"]}) is True

    def test_topological_sort_is_valid(self, graph):
        order = topological_sort(graph)
        assert order is not None
        assert set(order) == set(graph)
        position = {node: i for i, node in enumerate(order)}
        for node, neighbours in graph.items():
            for neighbour in neighbours:
                assert position[node] < position[neighbour]

    def test_topological_sort_cycle_returns_none(self):
        assert topological_sort({"A": ["B"], "B": ["A"]}) is None


class TestDijkstra:
    def test_distances(self):
        weighted = {
            "A": [("B", 1), ("C", 4)],
            "B": [("C", 2), ("D", 5)],
            "C": [("D", 1)],
            "D": [],
        }
        assert dijkstra(weighted, "A") == {"A": 0, "B": 1, "C": 3, "D": 4}

    def test_unreachable_omitted(self):
        assert dijkstra({"A": [], "B": []}, "A") == {"A": 0}


class TestNumIslands:
    def test_counts_islands(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        assert num_islands(grid) == 3

    def test_empty_grid(self):
        assert num_islands([]) == 0

    def test_all_water(self):
        assert num_islands([["0", "0"], ["0", "0"]]) == 0

    def test_diagonals_do_not_connect(self):
        assert num_islands([["1", "0"], ["0", "1"]]) == 2
