import random
import numpy as np

def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)

def mod_exp(x, y, N):
    # Time complexity of this function: o(n^2)

    returnVal = 1 #initializing return value

    # test if x mod N is equal to zero
    x = x % N
    if (x == 0):
        return 0

    # divide y by 2 until y = 0, while performing the modular exponentiation.
    while (y > 0):
        if((y & 1) == 1):
            returnVal = (returnVal * x) % N
        y = y >> 1
        x = (x * x) % N
    return returnVal

def fprobability(k):
    # Time complexity of this function: o(n)
    # probability of error is 1/(2^k) as given
    probability = 1 - (1 / (2 ** k))
    return probability

def mprobability(k):
    # Time complexity of this function: o(n)
    # probability of error is 3/(4^k) (given as 3/4 probability compared to 1/2 for the fermat test.
    probability = 1 - (3 / (4 ** k))
    return probability

def fermat(N, k):
    # Time complexity of this function: o(n^3)

    # this value "prime" allows me to keep track of values other than 1
    prime = True

    # loop for k values selected by user
    for x in range(k):
        rand = random.randint(0,5)
        exp = N - 1
        a = mod_exp(rand, exp, N) # a is a number given from the exponentiation of random int, N - 1, N
        if a > 1:
            # this checks to see if our modular exponentiation value is a number larger than one, meaning we have a component.
            prime = False

    # test to see if our number is composite or prime
    if prime == True:
        return 'prime'
    else:
        return 'composite'

def miller_rabin(N, k):
    # Time complexity of this function: o(n^3)

    #check preconditions for 2 and 3
    if N < 4:
        return 'prime'

    #check to see if the number is even and thus, composite
    if N % 2 == 0:
        return 'composite'

    #declaring a modular exponentiation value and an increment value
    modVal = N - 1
    incrementVal = 0

    #divide modvalue until we get an odd number
    while modVal % 2 == 0:
        incrementVal += 1
        modVal //= 2

    #for 'k' given by user, we perform a test similar to fermots test, then taking the square root and trying again
    for x in range(k):
        randVal = random.randrange(3, N - 1)
        exp = mod_exp(randVal, modVal, N)
        if exp == 1 or exp == N - 1:
            break
        for x in range(incrementVal - 1):
            exp = mod_exp(exp, 2, N)
            if exp == N - 1:
                print(5)
                break
        else:
            #if value returned in not 1, return composite
            return 'composite'
    return 'prime'
    # take the square root of a number until it is equal to something other than 1(mod N).
    # if we get -1(mod N), return prime(for now).
    # if we get anything else, return composite for sure.
