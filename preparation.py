import csv


def read_file(path: str, delimiter=","):
    with open(path) as file:
        return [row for row in csv.reader(file, delimiter=delimiter)]


def count_classes(data):
    counted_classes = []
    for i in range(len(data[0])):
        counted_classes.append(len(set([element[i] for element in data])))
    return counted_classes


def count_occurences(last_items):
    sets_of_elements = []
    for i in range(len(last_items[0])):
        sets_of_elements.append(list(set([val[i] for val in last_items])))
    occurances = [dict.fromkeys(element, 0) for element in sets_of_elements]
    for items in last_items:
        for i, j in enumerate(items):
            occurances[i][j] += 1
    return occurances
