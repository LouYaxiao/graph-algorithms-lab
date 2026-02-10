# graph-algorithms-lab

Reusable graph algorithms with tests and runnable demos.

## What you get
- Clean implementations in `src/graph_algorithms_lab/`
- Unit tests in `tests/` (pytest)
- CI checks: ruff + pytest (GitHub Actions)

## Quickstart
```bash
# (optional) create env
conda env create -f environment.yml
conda activate se-graph

pip install -e .
pytest -q
Algorithms
BFS (bfs.py)

Repo structure
src/graph_algorithms_lab/: library code

tests/: unit tests

.github/workflows/: CI

Roadmap
DFS, connected components

Dijkstra / Bellman-Ford

Union-Find, SCC

PageRank / random walk


Push：
```bat
git add README.md
git commit -m "docs: improve README for portfolio"
git push
