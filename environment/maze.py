import numpy as np

class Maze:
    def __init__(self):
        # 0: Path, 1: Wall, 2: Start, 3: Goal
        self.grid = np.array([
            [2, 0, 1, 0],
            [0, 0, 1, 3],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ])
        self.start_pos = (0, 0)
        self.goal_pos = (1, 3)

    def is_valid_move(self, position):
        rows, cols = self.grid.shape
        r, c = position
        return 0 <= r < rows and 0 <= c < cols and self.grid[r, c] != 1

    def get_feedback(self, position):
        if position == self.goal_pos:
            return 10  # Goal reached
        return -1  # Default move penalty
