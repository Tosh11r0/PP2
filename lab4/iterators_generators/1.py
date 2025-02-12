squares = [] #лист куда мы отправляем квадраты

def square(n): #функция квадрата
    i=1
    while i < n:
        squares.append(i**2)
        i+=1

m = int(input())
square(m)

sq = iter(squares)

for i in range (len(squares)): #функция вывода
    print (next(sq))
