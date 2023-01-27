# A simple python tool to calculate RSA private key (d) knowing the public exponent e

# This is Cryptomath Module, so we don't have to import the module everytime..
def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1
    if gcd(a, m) != 1:
        return None  # no mod inverse if a & m aren't relatively prime
    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3  # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


print("###############################################################################")
print("####################### RSA private key calculator ############################")
print("####################### find d knowing e, p and q  ############################")
print("###############################################################################")
print()

e = int(input("Provide the exponent e="))
p = int(input("Provide the prime p="))
q = int(input("Provide the prime q="))
print()
print("[*]Calculating d and n...")
print()

d = findModInverse(e, (p - 1) * (q - 1))
N = p * q

print("d =", d)
print("n =", N)
print()
print("[*]Success!")



