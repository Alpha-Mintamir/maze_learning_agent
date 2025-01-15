# 🧠 Maze Learning Agent

This project implements a **Q-learning agent** that learns to navigate a maze to reach a goal while maximizing its reward. It demonstrates the concept of **Learning Agents**, which combine performance, learning, and exploration to adapt to their environment.

---

## 🚀 Features
- **Q-Learning Algorithm** for reinforcement learning.
- **Customizable Maze Environment** with a start and goal position.
- Simulates an agent that learns optimal paths through trial and error.
- Provides detailed logs for learning and simulation steps.

---

## 🛠️ Project Structure
```
maze_learning_agent/
├── agent/
│   ├── __init__.py          # Package initializer
│   ├── maze.py              # Maze environment implementation
│   └── qlearning.py         # Q-learning agent implementation
├── main.py                  # Entry point to train and test the agent
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
├── venv/                    # Virtual environment folder
│   ├── bin/                 # Executables (Unix systems)
│   ├── Lib/                 # Libraries and dependencies (Windows)
│   ├── Scripts/             # Executables (Windows)
│   └── ...                  # Other virtual environment files
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/maze_learning_agent.git
cd maze_learning_agent
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Project
To train the agent and simulate its behavior:
```bash
python main.py
```

## 📝 Usage
- **Modify the Maze:** Customize the maze layout in `maze.py` by updating the `reward_map`.
- **Adjust Parameters:** Tweak hyperparameters like learning rate, discount factor, and exploration rate in `qlearning.py` for different behaviors.
- **Simulate:** Observe the agent's learning process and how it navigates the maze.

## 🧩 Concepts Explored
- **Reinforcement Learning (Q-Learning):** Training an agent to make decisions by interacting with an environment.
- **Learning Agents:** Combining performance, critic, learning element, and problem generator concepts.
- **Exploration vs Exploitation:** Balancing learning new paths versus using known paths.

## 💻 Dependencies
- Python 3.8+
- NumPy
- Matplotlib (optional, for advanced visualizations)

## 📂 Example Output
```bash
Starting simulation...
Step 1: Position = (0, 0), Reward = -1
Step 2: Position = (0, 1), Reward = -1
...
Step 10: Position = (3, 3), Reward = 10
Goal reached!
Total Reward: 3
```

## 🤝 Contributions
Contributions are welcome! Feel free to submit a pull request or open an issue for suggestions or bugs.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 📧 Contact
For any questions or feedback, reach out to:

**Author:** ChatGPT(lol)  
