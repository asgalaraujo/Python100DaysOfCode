def is_prime(num):
    divisores = []
    for i in range(1, num+1):
        if num % i == 0:
            divisores.append(i)
    if len(divisores) > 2 or num in (0, 1):
        return False
    else:
        print(f"Divisores de {num}: {divisores}")
        return True


for i in range(100):
    if is_prime(i):
        print(f"{i}, ")

