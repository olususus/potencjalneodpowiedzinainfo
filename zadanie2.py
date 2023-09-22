liczby = []
i = 1

while len(liczby) < 932:
    if i % 42 == 0:
        liczby.append(i)
    i += 1

print(liczby)