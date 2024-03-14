nums_str = input('enter a sequence of numbers: ')

while True:
    try:
        nums = [int(x) for x in nums_str.split() if x.isdigit()]
        break
    except:
        print('error')
        nums_str = input()
        
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def primes_max(nums):
    primes = []
    max_prime = -1
    for num in nums:
        if is_prime(num):
            primes.append(num)
    for prime in primes:
        if prime > max_prime:
            max_prime = prime
    return primes, max_prime

        
primes, max_prime = primes_max(nums)
print(primes)
print(max_prime)
print(sum(nums))