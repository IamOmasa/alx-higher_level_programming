def pow(a, b):
    result = 1

    if b > 0:
        for _ in range(b):
            result *= a
    elif b < 0:
        for _ in range(abs(b)):
            result /= a
    else:
        result = 1
    return result
