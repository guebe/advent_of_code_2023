from numpy.polynomial import Polynomial
i = 0
j = 0
for line in open("input").readlines():
    y = list(map(int,line.split()))
    poly = Polynomial.fit(list(range(len(y))), y, len(y)-1)
    i += round(poly(len(y)))
    j += round(poly(-1))
print(i)
print(j)
