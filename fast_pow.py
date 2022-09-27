# 快速幂
def fast_pow(x, n, p=1):
    rem = 1
    while n > 0:
        if n % 2:
            if p == 1:
                rem = rem * x 
            else:
                rem = (rem * x) % p 
        if p == 1:
            x = x * x
        else:
            x = (x * x) % p
        n //= 2
    return rem

# 循环求余
def remainder(x, a, p):
    rem = 1
    for _ in range(a):
        # rem = (rem * (x % p)) % p
        rem = (rem * x) % p
    return rem

# print(fast_pow(3,10) == 3 ** 10)
# print(fast_pow(10,16,13) == 10 ** 16 % 13)
print(remainder(100,3,13) == 100 ** 16 % 13)