def test(*args):
    print('test')
    print('тип args', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиция', i, arg)


test(12, "Privet", True, [1, 2, 3])


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n-1)
    return  n * factorial_n_minus_1

n = 7
result = factorial(n)
print(f"Факториал числа {n} равен {result}")