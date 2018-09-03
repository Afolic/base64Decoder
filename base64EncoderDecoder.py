import base64

print("Welcome to my base64 Cipher Text Encoder and Decoder!!!" "\n" "What would you like to do? Encrypt or decrypt" "\n")

text = raw_input("1 to Encrypt and 2 to Decrypt:")
#print text
if text == "1":
    plainText = raw_input("Enter the text you would like to crypt:" "\n")
    cipherText = base64.b64encode(plainText)
    print cipherText
    
elif text == "2":
    cipherText = raw_input("Enter the cipher text you would like to decrypt:")
    plainText = base64.b64decode(cipherText)
    print plainText
else:
    print "Usage: Press 1 for Encryption and 2 for Decryption"
    
