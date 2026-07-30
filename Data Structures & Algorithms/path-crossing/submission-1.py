class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}  # Starting position

        for move in path:
            # Update coordinates
            if move == "N":
                y += 1
            elif move == "S":
                y -= 1
            elif move == "E":
                x += 1
            else:
                x -= 1

            # Check if position was already visited
            if (x, y) in visited:
                return True

            visited.add((x, y))

        return False