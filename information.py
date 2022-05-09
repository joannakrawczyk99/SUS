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


def split_info():
    # tutaj robimy obliczenia z ogólnego wzoru na entropię
    counter = 0


def gain_ratio():
    # to takie ekstra+ ale warto dodać ze względu na jakieś tam dysproporcje w wartościach atrybutów, czy coś XD
    # GainRatio(X,T)=Gain(X,T)/SplitInfo(X,T)
    counter = 0