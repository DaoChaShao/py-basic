
left_number = 1


while left_number < 10:
    right_number = 1
    while right_number < 10:
        print(f'{left_number} * {right_number} = {left_number * right_number}', end='\t')
        right_number += 1
    left_number += 1
    print()
