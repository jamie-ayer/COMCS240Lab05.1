"""
- Create a new file as primemodule.py that includes the following functions:
- is_prime(n): returns True if n is a prime number, False otherwise
- print_primes(n): prints all prime numbers less than n
- get_primes(n): returns a list of all prime numbers less than n
"""
import math

def is_prime(v):
    
    if all(v % i != 0 for i in range(2, int(math.sqrt(v))+1)):
        return True
    else:
        return False
    
    
def print_primes(v):
            
    for i in range(2, v):
        if is_prime(i):
            print(i)
            
def get_primes(v):
    
    return [i for i in range(2, v) if is_prime(i)]
    