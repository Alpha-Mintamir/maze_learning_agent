from environment.maze import Maze
from agent.qlearning import QLearningAgent

# Create the maze environment
maze = Maze()

# Create a Q-Learning agent
agent = QLearningAgent(maze)

# Train the agent
agent.train(episodes=100)

# Run the simulation
agent.simulate()
