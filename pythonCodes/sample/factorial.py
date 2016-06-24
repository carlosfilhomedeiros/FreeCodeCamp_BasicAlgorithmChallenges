def fatorial(num):
    if (num == 1 or num == 0):
        return 1
    return (fatorial(num-1)*num)
