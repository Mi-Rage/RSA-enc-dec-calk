from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541
e = 9007

# find p and q on http://factordb.com
p = 3490529510847650949147849619903898133417764638493387843990820577
q = 32769132993266709549961988190834461413177642967992942539798288533

# calculate d in rsa_private_calk.py
d = 106698614368578024442868771328920154780709906633937862801226224496631063125911774470873340168597462306553968544513277109053606095

text = b"RSA is easy"
enc_flag = b'\x02\r\n\xca\x80\x15\xe5\xa3(\xbdY`\x00\x11\xd4/\xed\xa3\xa9\x91\xd8\x8eHKB\x93\\z\xdd\x821&\x04\xe5v0>\xd1\xd3J2\xb8\x06\x1ft_\xf5\xcb\x8a\x9f\xab\x9b\x92\x00'

print("plain =",text)

# enc some text
key = RSA.construct((n, e))
encryptor = PKCS1_OAEP.new(key)
encrypted = encryptor.encrypt(text)
print("enc =", encrypted)

# dec ecrypted text and flag
key = RSA.construct((n, e, d))
decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(encrypted)
print("dec =", decrypted)
decrypted = decryptor.decrypt(enc_flag)
print("dec flag =", decrypted)

