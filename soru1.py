#3'ün veya 5'in 1000'den kücük tüm katlarının toplamını bulun.
uck = list()
besk = list()
a = 0
while a < 1000:
    if a%3 == 0:
        uck.append(a)
    if a%5 == 0:
        besk.append(a)
    a += 1
uks=set(uck)
bks=set(besk)
print(sum(uks | bks))

