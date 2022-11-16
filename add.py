# a small program to confirm additive homomorphism of Paillier

import key_product
import encrypt
import decrypt


x = 26
k = key_product.main(x)
pub, pri = k[0], k[1]
print('---'*15)
i1 = eval(input('plaintext1:'))
c1 = encrypt.main(pub, i1)
# m1 = decrypt.main(pri, c1, pub[0])
print('ciphertext1：%i' % c1)
print('---'*15)
i2 = eval(input('plaintext2:'))
c2 = encrypt.main(pub, i2)
# m2 = decrypt.main(pri, c2, pub[0])
print('ciphertext2：%i' % c2)
print('---'*15)
print('ciphertext1 * ciphertext2： %i' % (c1*c2))
m3 = decrypt.main(pri, c1*c2, pub[0])
print('---'*15)
print('after decryption ：%i' % m3)
print('---'*15)
