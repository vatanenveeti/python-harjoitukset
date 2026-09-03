import random

lkm = int(input("Arpakuutioiden lukumäärä? "))
summa = 0

for i in range(lkm):
    summa = summa + random.randint(1,6)

print(f"Arpakuutioiden summa on {summa}.")