tup = ()
y = list(tup)
while (True):
    your_input = input("Enter smthing: ")
    if (your_input == ""):
        break
    y.append(your_input)

answer = all(y)
print(answer)