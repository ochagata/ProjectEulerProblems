__author__ = 'Ozer'


def get_sum_of_multiples():
    result = 0
    for j in range(0, 1000):
            is_multiple_of_three = (j % 3) == 0
            is_multiple_of_five = (j % 5) == 0

            if is_multiple_of_three and is_multiple_of_five:
                result += j
            elif is_multiple_of_three:
                result += j
            elif is_multiple_of_five:
                result += j

    return result

print(get_sum_of_multiples())