def prime_checker(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            print("It's not prime, it's divisible by ", i, " or ", i +2)
            return False
        i = i + 6
    print("Yup it's prime")
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
    if num % 2 == 0:
        print(num / 2)
        return num / 2
    i = (num // 2) - 1
    print(i)
    while i > 1:
        if num % i == 0:
            print(i)
            if prime_checker(i):
                print(i)
                return i
        i = i - 2
    # print("Number is prime") 


# def get_highest_prime_factor(num):
    # print(get_prime_factors(num)[-1])

# get_highest_prime_factor(600851475143)

# get_highest_prime_factor(799)
# get_highest_prime_factor(600851475143)
# get_highest_prime_factor(783)
get_highest_prime_factor(261)
# prime_checker(261)

