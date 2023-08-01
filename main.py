    #1
value = int(input("Введите число: "))
if (value%2==0):
        print(value, "Even number")
else:
        print(value, "Odd number")

    #2
value1 = int(input("Введите число: "))
if (value1%7==0):
    print(value1, "Number is multiple 7")
else:
    print(value1, "Number is not multiple 7")

    #3
value2 = int(input("Введите первое число: "))
value3 = int(input("Введите второе число: "))
if(value2<value3):
    print(value3)
else:
    print(value2)

    #4
value4 = int(input("Введите первое число: "))
value5 = int(input("Введите второе число: "))
if(value4<value5):
    print(value4)
else:
    print(value5)

    #5
value6 = int(input("Введите первое число: "))
value7 = int(input("Введите второе число: "))
value8 = input("Какую операцию хотите произвести (- + * /)? ")
if value8 == '+':
    print(value6, "+", value7, "=", value6 + value7)
elif value8 == '-':
    print(value6, "-", value7, "=", value6 - value7)
elif value8 == '*':
    print(value6, "*", value7, "=", value6 * value7)
elif value8 == '/':
    print(value6, "/", value7, "=", value6 / value7)