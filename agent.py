import random

class Agent:
    def __init__(self):
        pass

    def act(self):
        return random.choice(['action1', 'action2', 'action3'])

if __name__ == '__main__':
    agent = Agent()
    print(agent.act())
