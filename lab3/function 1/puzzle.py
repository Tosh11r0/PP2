def solve(num_heads, num_legs):
    for i in range(num_heads + 1):
        rabbits = num_heads - i
        if 2 * i + 4 * rabbits == num_legs:
            return i, rabbits
    return "No solution"  

num_heads = 35
num_legs = 94
result = solve(num_heads, num_legs)
if result != "No solution":
    chickens, rabbits = result
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print(result)
