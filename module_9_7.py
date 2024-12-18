def is_prime(func):
    def wrapper(*args):
        sum_2 = func(*args)
        k = 0
        for i in range(2, sum_2 // 2 + 1): # проверка на простое и составное число
            if sum_2 % i == 0:
                k += 1
        if k == 0:
            print('Простое')
        else:
            print('Составное')
        return sum_2
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)