#11
numbers = [5, 2, 9, 1, 7, 3]

roy1 = max(numbers)
roy2= min(numbers)

numbers.remove(roy1)
numbers.remove(roy2)

natija1 = max(numbers)
natija2 = min(numbers)

farq = natija1 - natija2

print("Qolgan ro'yxat:", numbers)
print("Farq:", farq)

#12
numbers = [5, -3, 0, 7, -1]

for i in range(len(numbers)):
    numbers[i] = -numbers[i]

print(numbers)

#13
a = [1, 2, 3, 4, 5, 6, 7]
n = 3
b = []

for i in range(0, len(a), n):
    b.append(a[i:i+n])

print(b)

#14
a = [1, 2, 2, 3, 1, 2]

natija = {}
for x in a:
    natija[x] = natija.get(x, 0) + 1

print(natija)
