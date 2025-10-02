import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return []
    elif min > max:
        return []
    elif quantity > (max - min + 1):
        return []

    random_set = set()
    while len(random_set) < quantity:
        random_set.add(random.randint(min, max))

    return sorted(random_set)


print("Ваші лотерейні числа:", get_numbers_ticket(1, 1000, 6))
print("Ваші лотерейні числа:", get_numbers_ticket(1000, 1, 6))
print("Ваші лотерейні числа:", get_numbers_ticket(99, 100, 3))