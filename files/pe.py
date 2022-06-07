def is_prime(num):
    for n in range(2, int(num**.5)+1):
        if num % n == 0:
            return False
    return True
