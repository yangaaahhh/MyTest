print("--------------1---------------")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [x for x in a if x % 2 == 0]
print(b)

print("--------------2---------------")
lm = lambda x: True if x % 2 == 0 else False
for i in range(1, 11):
    if lm(i):
        print(i)


