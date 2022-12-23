#oponant
# A for Rock, B for Paper, and C for Scissors
# You
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 lost, 3 draw, and 6 won


def read_file(filename : str):
    '''
    :param filename:
    :return data:
    '''
    with open(filename, 'r') as f:
        data = f.read()
    return data


def list_on_return(data):
    data_list = data.split('\n')
    return data_list


def make_2d_list(data: list):
    newlist = []
    for x in data:

        newlist.append([x,0])
    return newlist


def sym_chooser(data:list):
    for x in data:
        pass







def wld_classify(data:list):
    wld_list = []
    for x in data:
        if x[0] == 'C X' or x[0] == 'A Y' or x[0] == 'B Z':
            x[1] = 6
        if x[0] == 'A Z'  or x[0] == 'B X' or x[0] == 'C Y':
            x[1] = 0
        if x[0] == 'A X' or x[0] == 'B Y' or x[0] == 'C Z':
            x[1] = 3
        wld_list.append(x)
    return wld_list


def score_symbol(data:list):
    score_data = []
    for x in data:
        if 'X' in x[0]:
            x[1] = x[1] + 1
        if 'Y' in x[0]:
            x[1] = x[1] + 2
        if 'Z' in x[0]:
            x[1] = x[1] + 3
        score_data.append(x)
    return score_data


def add_scores(data):
    score_total = 0
    for x in data:
        score_total = score_total + x[1]
    return score_total


if __name__ == '__main__':
    input_data = read_file('input.txt')
    input_list = list_on_return(input_data)
    list_score = make_2d_list(input_list)
    wld_data = wld_classify(list_score)
    sym_data = score_symbol(wld_data)
    total_score = add_scores(sym_data)
    print(total_score)
