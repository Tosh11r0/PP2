def down(n):
    while (n>0):
        yield n
        n-=1

m = int(input())

for i in down(m):
    print(i)