
def square(n): #функция квадрата
    i=1
    while i < n:
        yield i**2 #создание генератора
        i+=1
    
m = int(input())

for num in square(m): #вывод квадратов
    print (num)


