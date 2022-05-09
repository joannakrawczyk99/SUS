from entropy import calc_entropy
from information import info_function, info_gain, split_info, gain_ratio
from preparation import read_file, count_occurences, count_classes

file = 'data/gieldaLiczby.txt'


if __name__ == "__main__":
    data = read_file(file)
    #print(len(data))

    entropy = calc_entropy(data)
    print(entropy)

    inf = info_function(data)
    print(inf)

    gain = info_gain(entropy, inf)
    print(gain)

    split_inf = split_info(data)
    print(split_inf)

    #ratio = gain_ratio(gain, split_inf)
    #print(ratio)
