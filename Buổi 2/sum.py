def digital_root(n):
    while n > 9:
        n = sum(int(count) for count in str(n))

    return n