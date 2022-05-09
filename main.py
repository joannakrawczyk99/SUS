from entropy import calc_entropy
from information import info_function, info_gain
from preparation import read_file, count_occurences, count_classes

file = 'data/gieldaLiczby.txt'


if __name__ == "__main__":
    data = read_file(file)
    #print(len(data))

    class_amount = count_classes(data)
    print(class_amount)

    occur = count_occurences(data)
    print(occur)

    entropy = calc_entropy(data)
    print(entropy)

    inf = info_function(data)
    print(inf)

    gain = info_gain(entropy, inf)
    print(gain)


