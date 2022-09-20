input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multifly_sum = 0
    for num in array:
        if num <= 1 or multifly_sum <= 1:
            multifly_sum += num
        else:
            multifly_sum *= num
    return multifly_sum


result = find_max_plus_or_multiply(input)
print(result)