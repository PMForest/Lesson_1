# Конвертация секунд в час:мин:сек

time = int(input("Введите кол секунд: "))

def convert(seconds):
    seconds = seconds % (24 * 3600)

    hour = seconds // 3600

    seconds %= 3600

    minutes = seconds // 60

    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


n = time

print(convert(time))
