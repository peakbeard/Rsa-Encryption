#
# @author JG
# @version 0.6.1
#
import secrets as sec

p = 32452127
q = 16260997


class Rsa:
    def __init__(self):
        self.p = p
        self.q = q
        self.N = self.p * self.q
        self.phiN = self.phi(self.p, self.q)

    def generate_keys(self):
        print('Generating new Rsa-Keys. This may take a while.')
        e = self.gen_e()
        public_key = [e, self.N]
        d, k = self.euklid(e, self.phiN)
        private_key = [d, self.N]
        print('Public key:\n' + str(public_key))
        print('Private key:\n' + str(private_key))
        return private_key, public_key

    def gen_e(self):
        phi = self.phiN
        e = sec.randbelow(phi-1) + 1
        while self.gcd(e, phi) != 1:
            e = sec.randbelow(phi - 1) + 1

        if self.gcd(e, phi) == 1:
            print('Public key generated. \nGenerating private key.')
            print(e)
        return e

    def phi(self, p, q):
        phi = (p - 1) * (q - 1)
        return phi

    def gcd(self, a, b):
        r = 1
        while r != 0:
            r = a % b
            a = b
            b = r
        return a

    def euklid(self, n, z):
        if n == 0:
            return (0, 1)
        else:
            x, y = self.euklid(z % n, n)
            return y - (z // n) * x, x



keys = Rsa()
keys.generate_keys()
