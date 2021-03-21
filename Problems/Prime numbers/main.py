prime_numbers = []
for i in range(2, 1001):
    test_list = []
    for j in range(2, i):
        test_list.append(i % j)
    if all(test_list):
        prime_numbers.append(i)
# print(prime_numbers)
