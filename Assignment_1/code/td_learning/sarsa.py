import numpy as np
seed = 2024
np.random.seed(seed)
import matplotlib.pyplot as plt
from td_learning.td_agent import TD_Agent

def avg_reward_line_plot(rewards_per_episode, num_episodes):
    avg_rewards = [np.mean(rewards_per_episode[max(0, i-50):i+1]) for i in range(num_episodes)]
    plt.plot(range(num_episodes), avg_rewards, color='red')
    plt.xlabel('Episodes')
    plt.ylabel('Average Reward (last 50 episodes)')
    plt.title('SARSA: Average Reward over Last 50 Episodes')
    plt.savefig('./avg_reward_sarsa_line.png')
    plt.clf()


class SARSA(TD_Agent):
    def __init__(self, env, args):
        self.env = env 
        self.n_actions = env.action_space.n
        self.n_states = env.observation_space.n
        self.alpha = args.alpha
        self.gamma = args.gamma
        self.num_episodes = args.num_episodes
        self.epsilon = args.epsilon
        self.epsilon_decay = args.epsilon_decay
        self.epsilon_min = args.epsilon_min
        self.save_sa_file = args.save_sa_file
        if args.test_sa:
            self.Q = np.load(args.save_sa_file)

    def make_action(self, state, test=True):
        # Hints:In testing mode, always select the action with the highest Q-value. 
        # In training mode, randomly select an action with a probability defined by epsilon, 
        # or otherwise select the best Q-value action. Finally, return the chosen action.

        pass 
    

    def train(self):
        self.Q = np.zeros((self.n_states, self.n_actions))
        rewards_per_episode = []

        for episode in range(self.num_episodes):
            state = self.env.reset()
            done = False
            episode_rewards = 0
            
            action = self.make_action(state, False)  
            
            while not done:
                next_state, reward, done, _ = self.env.step(action)
                episode_rewards += reward
                
                # Student Implementation: action selection strategy
                next_action = self.make_action(next_state, False)
                
                if done and reward == 0:
                    reward = -1
                
                # Student Implementation: Sarsa Update
                # Hints: Q(s, a) ← Q(s, a) + α * [r + γ * Q(s', a') - Q(s, a)]  


                
                state = next_state
                action = next_action
            
            self.epsilon = max(self.epsilon * self.epsilon_decay, self.epsilon_min)
            rewards_per_episode.append(episode_rewards)

            if episode % 50 == 0:
                print(f'Episode: {episode}, Epsilon: {self.epsilon:.4f}, Average Reward (last 50 episodes): {np.mean(rewards_per_episode[-50:]):.4f}')
        
        np.save(self.save_sa_file, self.Q)
        avg_reward_line_plot(rewards_per_episode, self.num_episodes)
        
        
    
