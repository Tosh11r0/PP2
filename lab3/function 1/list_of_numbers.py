def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(nums):
    return [num for num in nums if prime(num)]

nums = list(map(int, input("Введите числа: ").split()))
print(filter_prime(nums))
