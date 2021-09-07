# Write a Python function to sum all the numbers in a list

def sum_all_numbers(list):
    sum = 0
    for i in list:
        sum = sum + i

    return sum


numbers = [1.0, 2.2, 6.8]

print('Sum of numbers in list', numbers, 'is', sum_all_numbers(numbers))
