import time
import pyotp
import qrcode
key = pyotp.random_base32()
#totp = pyotp.TOTP(key)
#print(totp.now())
#time.sleep(30)
#print(totp.now())
#input_code = input("Enter 2FA Code: ")
#print(totp.verify(input_code))

#counter = 0 
#hotp = pyotp.HOTP(key)
#print(hotp.at(0))
#print(hotp.at(1))
#print(hotp.at(2))
#print(hotp.at(3))
#print(hotp.at(4))
#for _ in range(5):
#    print(hotp.verify(input("Enter code: "), counter))
#    counter +=1

uri = pyotp.totp.TOTP(key).provisioning_uri(name = "CARLOSSMITH123",
                                            issuer_name="GAUCH")
print(uri)
qrcode.make(uri).save("totp.png")
