def get_fibonacci(upper_bound):
    current = previous = 1
    ret = []
    while current <= upper_bound:
        ret.append(current)
        previous, current = current, current + previous

    return ret        
