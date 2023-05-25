#Найдите сумму цифр трехзначного числа.#
n = int(input("Введите трехзначное число "))
summa = 0
summa = summa + n % 10
n = n //10
summa = summa + n % 10
n = n //10
summa = summa + n % 10
print(summa)
