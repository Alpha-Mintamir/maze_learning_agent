import numpy as np
import random

class QLearningAgent:
    def __init__(self, maze, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.maze = maze
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate

        # Initialize Q-Table (state-action pairs)
        rows, cols = maze.grid.shape
        self.q_table = {
            (r, c): {action: 0 for action in ['up', 'down', 'left', 'right']}
            for r in range(rows)
            for c in range(cols)
        }

    def choose_action(self, position):
        if random.uniform(0, 1) < self.epsilon:
            # Explore: Choose a random action
            return random.choice(list(self.q_table[position].keys()))
        else:
            # Exploit: Choose the best action
            return max(self.q_table[position], key=self.q_table[position].get)

    def learn(self, current_state, action, reward, next_state):
        current_q = self.q_table[current_state][action]
        next_max_q = max(self.q_table[next_state].values())

        # Update Q-value using the Q-Learning formula
        self.q_table[current_state][action] = current_q + self.alpha * (
            reward + self.gamma * next_max_q - current_q
        )

    def move(self, position, action):
        action_map = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        new_position = (
            position[0] + action_map[action][0],
            position[1] + action_map[action][1]
        )
        return new_position if self.maze.is_valid_move(new_position) else position

    def train(self, episodes=100):
        for episode in range(episodes):
            position = self.maze.start_pos
def simulate(self):
    position = self.maze.start_pos
    total_reward = 0
    print("Starting simulation...")
    for step in range(20):  # Maximum of 20 steps for the simulation
        action = self.choose_action(position)  # Choose the best action
        position = self.move(position, action)  # Move based on the action
        reward = self.maze.get_feedback(position)  # Get reward for the new position
        total_reward += reward
        print(f"Step {step + 1}: Position = {position}, Reward = {reward}")
        
        if position == self.maze.goal_pos:  # Check if the goal is reached
            print("Goal reached!")
            break
    print(f"Total Reward: {total_reward}")
