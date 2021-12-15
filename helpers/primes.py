import math


def get_prime_factors(number):
    """Gets the prime factors of a number.
    From http://www.hsg-kl.de/faecher/inf/algorithmus/standard/primfak/index.php
    Für eine Primzahl p gibt es nur die Fälle: 1.Fall: 3∣p+1 oder 2.Fall: 3∤p+1.
    Im 1.Fall könnte p+2 eine Primzahl sein, da ungerade und nicht durch 3 teilbar.
    p+4 =p+1 + 3 ist aber wieder durch 3 teilbar, sodass der nächste Primzahl-Kandidat p+6 wäre.
    Im zweiten Fall muss p+2 durch 3 teilbar sein, weil p und p+1 es nicht waren.Man wird daher p+4 untersuchen.
    p+5 ist aber wieder durch 3 teilbar, sodass p+6 es nicht ist.p+6 kommt als Primzahl-Kandidat in Frage.
    Im ersten Fall sollte man also p+2 und dann p+6, im zweiten Fall p+4 und dann p+6 untersuchen.
    Die Primzahlkandidaten haben also abwechselnd eine Differenz von 2 und 4."""
    ret = {}
    if number <= 1:
        return ret

    while number % 2 == 0:
        add_prime_factor(ret, 2)
        number /= 2
    while number % 3 == 0:
        add_prime_factor(ret, 3)
        number /= 3
    t = 5
    diff = 2

    while t * t <= number:
        while number % t == 0:
            add_prime_factor(ret, t)
            number /= t
        t += diff
        diff = 6 - diff

    if number > 1:
        add_prime_factor(ret, number)

    return ret


def add_prime_factor(prime_factors, factor):
    """Adds aq prime factor to the specified dictionary.
    If the factor already exists, increases its exponent rather than adding it."""
    if factor <= 1:
        return
    if factor in prime_factors.keys():
        prime_factors[factor] += 1
    else:
        prime_factors[factor] = 1


def get_primes(upper_bound: int):
    """Gets prime numbers up to the specified limit."""
    prime_flags = [True] * (upper_bound + 1)
    prime_flags[0] = prime_flags[1] = False

    if upper_bound < 2:
        return []
    if upper_bound == 2:
        return [2]

    start_index = 2
    end_index = math.ceil(math.sqrt(upper_bound))

    while start_index <= end_index:
        for i in range(start_index * start_index, upper_bound + 1, start_index):
            prime_flags[i] = False

        while True:
            start_index += 1
            if start_index > end_index or prime_flags[start_index]:
                break

    return [i for i in range(2, upper_bound + 1) if prime_flags[i]]


def get_primes_generator(first_prime=2):
    """Gets a prime generator."""
    i = first_prime
    while True:
        done = True
        for l in range(2, int(math.sqrt(i) + 1)):
            if i % l == 0:
                done = False
                break
        if done:
            yield i
        i += 1


def get_next_prime(primes: list):
    """Gets the next prime in a list of specified primes."""
    if len(primes) == 0:
        return 2
    if len(primes) == 1:
        return 3

    ret = primes[-1] + 1
    while True:
        done = True
        for l in range(2, int(math.sqrt(ret) + 1)):
            if ret % l == 0:
                ret += 1
                done = False
                break
        if done:
            break

    return ret


def get_first_n_primes(count):
    """Gets the first n primes starting at 2."""
    ret = []
    for i in range(0, count):
        prime = get_next_prime(ret)
        ret.append(prime)

    return ret


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True

    for n in range(2, int(math.sqrt(number) + 1)):
        if number % n == 0:
            return False

    return True
