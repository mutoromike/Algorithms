def isPrime(number):
    return 2 in [number,2**number%number]

print(isPrime(19))