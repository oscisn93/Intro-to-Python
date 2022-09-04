prime_numbers = [i for i in range(2, 1000)]

for num in prime_numbers:
    for num2 in prime_numbers[num:]:
        if num2%num == 0 and num2 != num:
            prime_numbers.remove(num2)

for prime in prime_numbers:
    print(prime)