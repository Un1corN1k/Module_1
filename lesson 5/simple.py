def square(n_1):
    return n_1**2


def is_simple(n_2):
    help_number = int(n_2 ** 0.5)+1
    for i in range(2, help_number):
        if not n_2 % i:
            return False
    return True


result = list(filter(is_simple, range(51)))
print(result)
print(list(map(square, result)))

