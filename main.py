from sys import argv

from functions.fit import fit
from functions.train import train


if __name__ == '__main__':
    action = argv[1]

    if action == 'train':
        dataset = argv[2]
        train(dataset)
    elif action == 'fit':
        fit()
    else:
        raise Exception('Specify an action and a dataset or file with tweets in function of the action')
