import numpy as np
import argparse
import gym
from td_learning.q_learning import Q_Learning
from td_learning.sarsa import SARSA

seed = 2024

def parse():
    parser = argparse.ArgumentParser(description="DRL Assignment 1")
    parser.add_argument('--test_ql', action='store_true', help='whether test q-learning')
    parser.add_argument('--test_sa', action='store_true', help='whether test sarsa')
    try:
        from argument import add_arguments
        parser = add_arguments(parser)
    except:
        pass
    args = parser.parse_args()
    return args


def test(env, td_agent, num_episodes=100):
    rewards = []
    env.seed(seed)
    for _ in range(num_episodes):
        state = env.reset()
        done = False
        episode_reward = 0.0
        while not done:
            action = td_agent.make_action(state)
            next_state, reward, done, _ = env.step(action)
            state = next_state
            episode_reward += reward
        
        rewards.append(episode_reward)

    print('Run %d episodes'%(num_episodes))
    print('Average reward is:',np.mean(rewards))


def run(args):
    env = gym.make('FrozenLake-v1', is_slippery=True)

    if args.test_ql:
        td_ql = Q_Learning(env,args)
        test(env, td_ql)

    if args.test_sa:
        td_sa = SARSA(env, args)
        test(env, td_sa)


if __name__ == '__main__':
    args = parse()
    run(args)


