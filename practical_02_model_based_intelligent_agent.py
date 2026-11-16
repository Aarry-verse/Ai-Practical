# Practical 2: Model-Based Intelligent Agent

class Agent:
    def __init__(self):
        self.visited = []

    def move(self, x, y, obstacles):
        self.visited.append((x, y))

        if (x+1, y) not in obstacles and (x+1, y) not in self.visited:
            return x+1, y
        elif (x, y+1) not in obstacles and (x, y+1) not in self.visited:
            return x, y+1
        else:
            return x, y
agent = Agent()
obstacles = [(1, 0)]
print("Initial Position:", (0, 0))
print("Next Position:", agent.move(0, 0, obstacles))
print("Memory:", agent.visited)
