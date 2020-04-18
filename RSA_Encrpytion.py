from random import randrange, getrandbits
class RSA_Encryption:
  def __init__ (self):
    self.p = 0
    self.q = 0
    self.public_key = ()
    self.private_key = ()

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

  def gcd(self,a,b): # Finding gcd using Euclid Algorithm
    remainder = 0
    while b != 0:
      rem = a % b
      a = b
      b = rem
    return a

  def inverse(self,a,b): # Finding inverse of a mod b using Extended Euclid Algorithm
    if self.gcd(a,b) != 1:
      a //= self.gcd(a,b)
      b //= self.gcd(a,b)
    copy_b = b
    x = 1
    y = 0
    if b == 1:
      return 0
    while a > 1:
      q = a // b
      t = b
      b = a % b
      a = t
      t = y
      y = x - q * y
      x = t
    if x < 0:
      x = x + copy_b
    return x

  def generate_key(self):
    n = self.p * self.q
    k = (self.p-1) * (self.q-1)
    e = randrange(2,k-1)
    while self.gcd(e,k) != 1:
      e = randrange(1,k)
    d = self.inverse(e,k)
    if d < 0:
      d = k - d
    self.public_key = (n,e)
    self.private_key = (n,d)

  def modular_pow(self,base,exponent,modulus):
    result = 1
    while exponent > 0:
      if exponent % 2 == 1:
        result = (result * base) % modulus
      exponent = exponent >> 1
      base = (base * base) % modulus
    return result

  def encrypt(self,password):
    n, key = self.public_key
    return [self.modular_pow(ord(each),key,n) for each in password]

  def decrypt(self,pv,cipher):
    self.private_key = pv
    n, key = self.private_key
    return ''.join([chr(self.modular_pow(each,key,n)) for each in cipher])



