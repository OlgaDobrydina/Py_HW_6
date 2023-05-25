m = int (input("Введите год "))
if m % 4 == 0 and m % 100 != 0 or m % 400 == 0:
    print("yes")
else:
    print("no")    

