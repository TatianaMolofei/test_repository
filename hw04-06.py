# Введите число. Если это число делиться на 1000 без остатка, то выведите на экран "millennium"

print('Введите число')
num1 = input()

if int(num1) % 1000 == 0:
    print('millennium')