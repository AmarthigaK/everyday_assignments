import random

print(random.random())
print(random.randint(4,35))
print(random.randrange(11,20,10))

print(random.choice("AmarthigaK"))
print(random.choice((12,33,45,67,78)))
print(random.choice(("amar","div","kowsi")))

n=[12,23,45,67,65,43]
print(random.shuffle(n))