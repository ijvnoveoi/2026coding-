#week13-2.py
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))  # row, col, steps
        visited = set()
        visited.add((entrance[0], entrance[1]))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while q:
            r, c, steps = q.popleft()

            # Check if current cell is an exit
            if (r, c) != (entrance[0], entrance[1]) and (
                r == 0 or c == 0 or r == m - 1 or c == n - 1
            ):
                return steps

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    maze[nr][nc] == '.' and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))

        return -1
