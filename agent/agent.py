import random

class Agent:
    def __init__(self, maze):
        self.maze = maze
        self.position = maze.start_pos
        self.actions = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }

    def move(self, action):
        new_position = (
            self.position[0] + action[0],
            self.position[1] + action[1]
        )
        if self.maze.is_valid_move(new_position):
            self.position = new_position
        return self.position

    def simulate(self):
        print("Starting simulation...")
        total_reward = 0

        for step in range(10):  # Max steps
            action = random.choice(list(self.actions.values()))
            self.move(action)
            reward = self.maze.get_feedback(self.position)
            total_reward += reward

            print(f"Step {step + 1}: Position = {self.position}, Reward = {reward}")
            if self.position == self.maze.goal_pos:
                print("Goal reached!")
                break

        print("Total Reward:", total_reward)
