import random

def highestfactor(x, y):
    while y != 0:
        x, y = y, x % y
    return a
def inv(e, ratio):
    d = 0
    value_x = 0
    value_x2 = 1
    value_y = 1
    rat = ratio
    while e > 0:
        a = rat/e
        b = rat - a * e
        rat = e
        e = b
        x = value_x2- a* value_x
        y = d - a * value_y
        value_x2 = value_x
        value_x = x
        d = value_y
        value_y = y
    if rat == 1:
        return d + ratio

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in xrange(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(temp1, temp2):
    if not (is_prime(temp1) and is_prime(temp2)):
        raise ValueError('Both numbers must be prime.')
    elif temp1 == temp2:
        raise ValueError('p and q cannot be equal')
    prod = temp1 * temp2

    ratio = (temp1-1) * (temp2-1)
    e = random.randrange(1, ratio)

    g = highestfactor(e, ratio)
    while g != 1:
        e = random.randrange(1, ratio)
        g = highestfactor(e, ratio)
    d = inv(e, ratio)
    return ((e, prod), (d, prod))

def encrypterfunction(mult, ptx):
    key, n = mult
    cipher = [(ord(char) ** key) % n for char in ptx]
    return cipher

def decrypterfunction(mult, ctx):
    key, n = mult
    plain = [chr((char ** key) % n) for char in ctx]
    return ''.join(plain)
    

if __name__ == '__main__':
    p = int(raw_input("Enter a prime "))
    q = int(raw_input("Enter another prime  "))
    public, private = generate_keypair(p, q)
    message = raw_input("Enter a message to encrypterfunction with your private key: ")
    encrypterfunctioned_msg = encrypterfunction(private, message)
    print "Your encrypterfunctioned message is: "
    print ''.join(map(lambda x: str(x), encrypterfunctioned_msg))
    print "Your message is:"
    print decrypterfunction(public, encrypterfunctioned_msg)
