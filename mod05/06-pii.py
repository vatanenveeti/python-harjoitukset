import random

N = int(input("Anna pisteiden kokonaismäärä: "))
i = 0
n = 0

while i < N:
    luku_x = random.uniform(-1,1)
    luku_y = random.uniform(-1,1)
    if luku_x**2 + luku_y**2 < 1:
        n = n + 1
    i = i + 1

pii = 4*n/N
print(pii)