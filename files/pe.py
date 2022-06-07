def is_prime(num):
    for n in range(2, int(num**.5)+1):
        if num % n == 0:
            return False
    return True

def factorize(num, start = 2):
    if num == 1: return []
    factors = []

    n = start
    for n in range(start, int(num**.5) + 1):
        if num % n == 0:
            factors += [[n] + factor for factor in factorize(num//n, n)]

    factors += [[num]]
    return factors
