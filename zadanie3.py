def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def nww(a, b):
    return a * b // nwd(a, b)

x = int(input("Podaj pierwszą liczbę: "))
y = int(input("Podaj drugą liczbę: "))

nww_result = nww(x, y)

print(f"Najmniejsza wspólna wielokrotność ({x}, {y}) wynosi {nww_result}")