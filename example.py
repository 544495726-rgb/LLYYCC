# Example usage of the AI agent

from agent import Agent

if __name__ == '__main__':
    agent = Agent()
    action = agent.act()
    print(f'The agent decided to take: {action}')
