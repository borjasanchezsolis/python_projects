numbers = [1, 4, 6, 3, 6, 2, 6]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
