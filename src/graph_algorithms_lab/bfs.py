from __future__ import annotations

from collections import deque
from collections.abc import Hashable, Iterable


def bfs(adj: dict[Hashable, Iterable[Hashable]], start: Hashable) -> list[Hashable]:
    """Return BFS visit order from start in an unweighted graph."""
    visited: set[Hashable] = {start}
    order: list[Hashable] = []
    q: deque[Hashable] = deque([start])

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)

    return order
