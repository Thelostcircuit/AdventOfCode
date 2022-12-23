
def read_file(in_file):
    with open(in_file, 'r') as f:
        contents = f.read()
    return contents


def data_to_list(data):
    list = data.split('\n')
    return list

def list_to_int(data):
    int_list = []
    for x in data:
        if x != '':
            int_list.append(int(x))
        else:
            int_list.append('')
    return int_list


def make_list_totals(data):
    total = 0
    total_list = []
    for x in data:
        if x != '':
            total = total + int(x)
        else:
            total_list.append(total)
            total = 0
    return total_list


if __name__ == '__main__':
    input_data = read_file('input-1.txt')
    data_list = data_to_list(input_data)
    int_list = list_to_int(data_list)
    list_of_totals = make_list_totals(int_list)
    list_of_totals.sort()
    n = len(list_of_totals) - 3
    print(list_of_totals[n:])
    top3 = sum(list_of_totals[n:])
    print(list_of_totals)

    print(top3)


