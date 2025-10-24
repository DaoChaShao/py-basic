
index = 10
right_number = 9

while index > 0:
    left_number = 1
    while left_number < index:
        print(f'{left_number} * {right_number} = {left_number * right_number}', end='\t')
        left_number += 1
    right_number -= 1
    index -= 1
    print()
