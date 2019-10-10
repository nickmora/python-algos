def prime_checker(num):
    is_prime = True
    # i = 2
    # while i < num//2:
    #     if num % i == 0:
    #         is_prime = False
    #     i = i + 1
    # # print(is_prime)
    # return is_prime
    
# prime_checker(31)
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    
    return True

def get_prime_factors(num):
    prime_factors = []
    i = 2
    while i < num:
        if(num % i == 0 and prime_checker(i)):
            prime_factors.append(i)
        i = i + 1
    print(prime_factors)
    return prime_factors

# get_prime_factors(132)

def get_highest_prime_factor(num):
    print(get_prime_factors(num)[-1])

get_highest_prime_factor(600851475143)