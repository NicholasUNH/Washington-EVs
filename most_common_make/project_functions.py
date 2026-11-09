"""
Create a program that will analyze data read from a CSV file
and output various functions
Developer: Brenton
Collaborator: Nick O.
"""

def most_common(filename):
    """
    determine the most prevalent electric vehicle make.
    parameters: str
    output: str
    """

    pop_makes = {}
    with open(filename, 'r', encoding='utf8') as f_in:
        next(f_in)
        for line in f_in:
            line_lst = line.strip().split(',')
            car = line_lst[6]
            if car not in pop_makes:
                pop_makes[car] = 1
            elif car in pop_makes:
                pop_makes[car] = pop_makes[car] + 1
        car_makes = pop_makes.keys()
        key_with_max = list(car_makes)[0]
        for vehicle in car_makes:
            if pop_makes[vehicle] > pop_makes[key_with_max]:
                key_with_max = vehicle
    return key_with_max


def test_most_common():
    """
    Test most_common() with test csv
    """
    print('The most popular make is:')
    cars = 'data_test.csv'
    actual = most_common(cars)
    expected = 'TESLA'
    print(actual, expected)

test_most_common()
