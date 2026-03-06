def add_arguments(parser):
    '''
    Add your arguments here if needed. The TAs will run test.py to load
    your default arguments.

    For example:
        parser.add_argument('--alpha', type=float, default=0.1, help='Learning rate, how much new info overrides old.')
        parser.add_argument('--gamma', type=float, default=0.99, help='Discount factor, importance of future rewards.')
    '''

    parser.add_argument('--alpha', type=float, default=0.1)
    parser.add_argument('--gamma', type=float, default=0.99)
    parser.add_argument('--epsilon', type=float, default=1.0)
    parser.add_argument('--epsilon_decay', type=float, default=0.995)
    parser.add_argument('--epsilon_min', type=float, default=0.01)
    parser.add_argument('--num_episodes', type=int, default=1000)
    parser.add_argument('--save_ql_file', type=str, default="checkpoints/q_table.npy")
    parser.add_argument('--save_sa_file', type=str, default="checkpoints/sarsa_q_table.npy")
    return parser