import math

from preparation import count_occurences


def calc_entropy(data):
    prob = []
    for element in count_occurences(data)[-1].values():
        prob.append(element / len(data))
    entropy = 0
    for p in prob:
        if p > 0:
            entropy += p * math.log(p, 2)
    return -entropy
