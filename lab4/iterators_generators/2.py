def even(n): #функция четных чисел
    i=1
    while i < n:
        if (i%2 == 0):
            yield i
        i+=1

m = int(input())

for num in even(m):
    print (num)