def derivative(n): #функция четных чисел
    i=1
    while i < n:
        if (i%3 == 0 and i%4 == 0):
            yield i
        i+=1

m = int(input())

for num in derivative(m):
    print (num)