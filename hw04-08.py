# Ввести строку. Если длина строки больше 10 символов, то создать новую строку, равную текущей, с 3 восклицательными
# знаками в конце ('!!!') и вывести на экран. Если меньше 10, то вывести на экран второй символ строки.

string = input()

if int(len(string)) > 10:
    string = f'{string}!!!'

else:
    string = string[1]

print(string)

