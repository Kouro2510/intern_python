def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))


text = "-1 -4 -5 -77 -9 0"
print(high_and_low("87 3 -5 42 -1 0 0 -9 4 7 4 -4"))
