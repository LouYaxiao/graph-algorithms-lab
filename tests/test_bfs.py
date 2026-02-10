from graph_algorithms_lab.bfs import bfs


def test_bfs_simple():
    adj = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    out = bfs(adj, "A")
    assert out[0] == "A"
    assert set(out) == {"A", "B", "C", "D"}
