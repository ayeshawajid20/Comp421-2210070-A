import crypto
from crypto.PublicKey import RSA
from crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange

encrypted = publickey.encrypt('encrypt this message', 32)
#message to encrypt is in the above line 'encrypt this message'

print('encrypted message:', encrypted) #ciphertext
f = open ('encryptedfile.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryptedfile.txt', 'r')
message = f.read()


decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print('decrypted', decrypted)

f = open ('encryptedfile.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()
