import itertools


def tax_calc(data: list, wanted_sum: int):
    for numbers in itertools.combinations(data, 3):
        if sum(numbers) == wanted_sum:
            return [data.index(number) for number in numbers]


def get_real_input_data():
    with open('01/01_input.txt') as f:
        return [int(x) for x in f]


def multiply_list(my_list):
    # Multiply elements one by one
    result = 1
    for x in my_list:
        result = result * x
    return result


if __name__ == '__main__':

    input_data = [1721, 979, 366, 299, 675, 1456]
    input_data = get_real_input_data()

    positions = tax_calc(input_data, 2020)
    entries = [input_data[pos] for pos in positions]
    mul = multiply_list(entries)
    print(f"The entries are: {entries}")
    print(f"multiplied are: {mul}")