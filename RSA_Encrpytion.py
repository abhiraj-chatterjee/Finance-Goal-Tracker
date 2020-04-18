from random import randrange, getrandbits
class RSA_Encryption:
  def __init__ (self):
    self.p = 0
    self.q = 0

  def is_prime(self,n,k=128):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

  def generate_prime_candidate(self,length):
    k = getrandbits(length)
    k |= (1 << length - 1) | 1
    return k

  def generate_prime_number(self,length = 1024):
    x = 4
    while not self.is_prime(x, 128):
        x = self.generate_prime_candidate(length)
    return x

  def generate_numbers(self): # Generate two large prime numbers based on Miller-Rabin Primality Test
    self.p = self.generate_prime_number()
    self.q = self.generate_prime_number()


