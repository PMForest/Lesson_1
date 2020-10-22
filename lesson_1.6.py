run_man = int(input("Введите количество км. в 1 день: "))
end_run = int(input("Введите макс. количество км в день: "))

day = 1

while run_man <= end_run:
    day = day + 1
    run_man = run_man * 1.1

    print("Количество дней до результата = ", day)
