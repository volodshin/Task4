def bank():
    n = int(input("Введіть число: "))
    years = int(input("Введіть рік: "))

    vidsotok = 1 / 10
    money = n * vidsotok

    i = 0

    while i < years:
        n += money
        i += 1

    print(round(n, 2))


print(bank())