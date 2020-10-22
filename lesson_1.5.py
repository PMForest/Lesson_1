user_profit = int(input("Введите сумму прибыли: "))
user_cost = int(input("Введите сумму издержек: "))

if user_profit > user_cost:
    print('Вы наконец можете выдать сотрудникам "ЗП"')
    print('Коэффицент рентабельности равен: ', user_profit / (user_profit + user_cost ))
    man = int(input("Введите кол. сотрудников: "))
    print('Прибыль на одного сотрудника: ', user_profit / man)
else:
    print('Вы "ПОТРаЧЕнЫ" Бегите!')



