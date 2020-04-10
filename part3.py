def factoriel(k):
    l = 1
    for i in range(1, k + 1):
        l = i * l
    return l


print(factoriel(7))


def som_fact(l):
    f = 0
    for i in (l):
        temp = factoriel(i)
        f = f + temp
    return f

print(som_fact([1,7]))