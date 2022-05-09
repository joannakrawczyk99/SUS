import math

from entropy import calc_entropy
from preparation import count_occurences


def info_function(data):
    last_occurs_values = list(count_occurences(data)[-1].values())
    sum = 0
    for i in range(len(last_occurs_values)):
        sum = sum + last_occurs_values[i]/len(data) * calc_entropy(data)
    return sum


def info_gain(entropy_result, info_function_result):
    return entropy_result - info_function_result


def split_info(data):
    occ = count_occurences(data)
    atr_entropy = []
    for i in range(len(occ) - 1):
        atr_entropy.append(calc_entropy(data[i]))
    return atr_entropy


def gain_ratio(gain, split, data):
    ratio = []
    occ = count_occurences(data)
    for i in range(len(occ) - 1):
        ratio.append(gain/split[i])
    return ratio