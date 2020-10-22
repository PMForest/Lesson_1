user_number = int(input("Введите целое положительное число: "))

number = user_number
res = -1
while number > 10:
    x = number % 10
    number //= 10
    if x > res:
        res = x
print(res)
