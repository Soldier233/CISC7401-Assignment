import numpy as np
seed = 2024
np.random.seed(seed)
import matplotlib.pyplot as plt
from td_learning.td_agent import TD_Agent

def avg_reward_line_plot(rewards_per_episode, num_episodes):
    avg_rewards = [np.mean(rewards_per_episode[max(0, i-50):i+1]) for i in range(num_episodes)]
    plt.plot(range(num_episodes), avg_rewards, color='blue')
    plt.xlabel('Episodes')
    plt.ylabel('Average Reward (last 50 episodes)')
    plt.title('Q-Learning: Average Reward over Last 50 Episodes')
    plt.savefig('./avg_reward_q_learning_line.png')
    plt.clf()


class Q_Learning(TD_Agent):
    def __init__(self, env, args):
        self.env = env
        self.n_actions = self.env.action_space.n
        self.n_states = self.env.observation_space.n
        self.alpha = args.alpha
        self.gamma = args.gamma
        self.num_episodes = args.num_episodes
        self.epsilon = args.epsilon
        self.epsilon_decay = args.epsilon_decay
        self.epsilon_min = args.epsilon_min
        self.save_ql_file = args.save_ql_file
        self.Q = np.zeros((self.n_states, self.n_actions))

        if args.test_ql:
            self.Q = np.load(args.save_ql_file)


    def make_action(self, state, test=True):
        # Hints:In testing mode, always select the action with the highest Q-value. 
        # In training mode, randomly select an action with a probability defined by epsilon, 
        # or otherwise select the best Q-value action. Finally, return the chosen action.
        if test:
            return np.argmax(self.Q[state])
        else:
            if np.random.rand() < self.epsilon:
                return np.random.choice(self.n_actions)
            else:
                return np.argmax(self.Q[state])
    

    def train(self):
        rewards_per_episode = []
        for episode in range(self.num_episodes):
            state = self.env.reset()
            done = False
            episode_rewards = 0
            while not done:
                # Student Implementation: action selection strategy
                action = self.make_action(state,False)
                
                next_state, reward, done, _ = self.env.step(action)
                episode_rewards += reward
                
                if done and reward == 0:
                    reward = -1
                
                # Student Implementation: Q_learning_update
                # Hints: Q(s, a) ← Q(s, a) + α * [r + γ * max(Q(s', a')) - Q(s, a)]
                best_next_q = np.max(self.Q[next_state])
                self.Q[state, action] += self.alpha * (reward + self.gamma * best_next_q - self.Q[state, action])
                
                state = next_state
            
            # self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)
            rewards_per_episode.append(episode_rewards)

            if episode % 50 == 0:
                print(f'Episode: {episode}, Epsilon: {self.epsilon:.4f}, Average Reward (last 50 episodes): {np.mean(rewards_per_episode[-50:]):.4f}')
        
        np.save(self.save_ql_file, self.Q)

        avg_reward_line_plot(rewards_per_episode, self.num_episodes)
        
        
        


    
    




