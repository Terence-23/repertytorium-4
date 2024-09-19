def min_max(l):
    min = l[0]
    max = l[0]
    max_i = 0
    min_i = 0
    for i,v in enumerate(l[1:], 1):
        if v > max:
            max_i, max = i, v
        elif v < min:
            min_i, min = i, v


def qsort(l, low, high):
    if (low < high):
        pivot = l[high]
        i = low-1
        for j in range(low, high):
            if l[j] <= pivot:
                i+=1
                (l[j], l[i]) = l[i], l[j]
        l[i+1], l[high] = l[high], l[i+1]
        qsort(l, low, i)
        qsort(l, i+2, high)




from random import shuffle, randint

N = 10
L = 100

for i in range(N):
    # print(i)
    l = [randint(1, 100) for _ in range(L)]
    # print(l)
    sorted = l[::]
    sorted.sort()
    qsort(l, 0, len(l)-1)
    assert l == sorted