def find_max(numbers):
    maximal = numbers[0]
    for number in numbers:
        if number > maximal:
            maximal = number
    return maximal