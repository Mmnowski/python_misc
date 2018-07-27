def genPrime():
    primes = [1]
    test = 2
    while True:
        is_prime = True
        if len(primes) > 2:
            for n in range(len(primes)-1):
                if test % primes[n+1] == 0:
                    is_prime = False
                    break
        if is_prime is True:
            primes.append(test)
            next = test
            yield next
        test += 1


f = genPrime()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
