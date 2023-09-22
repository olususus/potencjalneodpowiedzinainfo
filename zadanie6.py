def czy_pierwsza(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

a = int(input("Podaj długość pierwszego boku: "))
b = int(input("Podaj długość drugiego boku: "))
c = int(input("Podaj długość trzeciego boku: "))

if czy_pierwsza(a) and a + b > c and a + c > b and b + c > a:
    print("Można zbudować trójkąt.")
else:
    print("Nie można zbudować trójkąta.")