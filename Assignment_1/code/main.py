from td_learning.q_learning import Q_Learning
from td_learning.sarsa import SARSA
from test import test
import gym
import argparse

def parse():
    parser = argparse.ArgumentParser(description="DRL Assignment 1: TD Learning")
    parser.add_argument('--env_name', default="TD Learning", help='environment name')
    parser.add_argument('--train_ql', default='True', action='store_true', help='whether train q-learning')
    parser.add_argument('--train_sa', default='True', action='store_true', help='whether train sarsa')
    parser.add_argument('--test_ql', action='store_true', help='whether test q-learning')
    parser.add_argument('--test_sa', action='store_true', help='whether test sarsa')
    try:
        from argument import add_arguments
        parser = add_arguments(parser)
    except:
        pass
    args = parser.parse_args()
    return args


def main(args):

    env = gym.make('FrozenLake-v1', is_slippery=True)

    if args.train_ql:
        td_ql = Q_Learning(env,args)
        td_ql.train()

    if args.train_sa:
        td_sa = SARSA(env, args)
        td_sa.train()

    if args.test_ql:
        td_ql = Q_Learning(env,args)
        test(env, td_ql)
        
    if args.test_sa:
        td_sa = SARSA(env,args)
        test(env, td_sa)
        
if __name__ == '__main__':
    args = parse()
    main(args)
