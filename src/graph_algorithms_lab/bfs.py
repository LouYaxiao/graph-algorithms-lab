from collections import deque
from typing import Dict, Hashable, Iterable, List


def bfs(adj: Dict[Hashable, Iterable[Hashable]], start: Hashable) -> List[Hashable]:
    visited = {start}
    order: List[Hashable] = []
    q = deque([start])

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)

    return order
