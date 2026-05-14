#week12-2a.py
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()
        visited.add(0)
        while stack:
            now = stack.pop()
            for k in rooms[now]:
                if k in visited: continue
                stack.append(k)
                visited.add(k)
        return len(rooms) == len(visited)
