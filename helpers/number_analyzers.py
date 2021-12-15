from helpers.primes import get_prime_factors


def is_palindrome(number: int):
    number_as_string = str(number)
    return number_as_string == number_as_string[::-1]


def least_common_multiple(numbers):
    max_factors = {}
    for number in numbers:
        prime_factors = get_prime_factors(number)
        for base, exponent in prime_factors.items():
            if base not in max_factors.keys() or max_factors[base] < exponent:
                max_factors[base] = exponent

    ret = 1
    for base, exponent in max_factors.items():
        ret *= base ** exponent

    return ret


def mult(iterable):
    result = 1
    for item in iterable:
        result *= item
    return result


def least_common_multiple_from_range(limit):
    # get product of all numbers in range
    num = mult(range(1, limit + 1))

    # reduce num to minimal which divides by all numbers in range
    while True:
        for n in range(2, limit + 1):        # for numbers 2...20
            if num % n == 0:
                num_new = num // n
                # check if it divides by all numbers
                for m in range(limit, 0, -1):
                    if num_new % m != 0:
                        break
                else:
                    # new num < previous num, repeat cycle
                    num = num_new
                    break
        else:
            # we cannot reduce num any more
            return num


def sum_of_numbers(upperBound) -> int:
    return int(upperBound * (upperBound + 1) / 2)


def sum_of_squares(upperBound) -> int:
    return int(upperBound * (upperBound + 1) * (2 * upperBound + 1) / 6)


def get_divisors(number) -> list:
    # Get all prime factors x^y
    prime_factors = get_prime_factors(number)

    # For each prime factor calculate the possible numbers (x^1, x^2, ... x^y)
    factors = list([])
    for base in prime_factors:
        numbers = [base ** i for i in range(1, prime_factors[base] + 1)]
        factors.append(numbers)

    if len(factors) == 0:
        return []

    # Append 1 to result set
    factors[0].append(1)
    result_set = factors[0]
    for i in range(1, len(factors)):
        # Append 1 to temporary set
        factors[i].append(1)
        set = factors[i]

        # Multiply all members of the result set with all members of the temporary set
        result_set = [r * s for r in result_set for s in set]

    return result_set


def get_divisors_without_self(number) -> list:
    ret = get_divisors(number)
    if number in ret:
        ret.remove(number)

    return ret
