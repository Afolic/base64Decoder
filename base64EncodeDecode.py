import base64

print "Would you like to encrypt or decrypt?"

print raw_input(" Type 1 for Encrypt or 2 for Decrypt:")

string = base64.decodestring("eyJVc2VyIjoiIiwiQWRtaW4iOiJUcnVlIiwiTUFDIjowZTc2ODI2MTI1MTkwMzgyMDkzNzM5MDY2MTY2ODU0N30=")

print (string)
