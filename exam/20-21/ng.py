def ng(a, n):
    z = (a[i:] for i in range(n))
    return zip(*z)
print(list(ng([1,2,3,4,5,6], 4)))