prime_numbers = [2]
for i in range(3, 1000, 2):
    if all((i % j for j in range(3, i, 2))):
        prime_numbers.append(i)
