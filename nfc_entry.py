import nfc,binascii,requests,random
# import binascii
# import requests
# import random


clf = nfc.ContactlessFrontend('usb')
print('カードを置いてください：')
try:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
finally:
    clf.close()

idm = binascii.hexlify(tag.idm)

#場所を「1～3」の中から適当に選択
place_id = random.randint(1,3)

# data = {
#     "id":idm,
#     "place_id":place_id
# }

idm = idm.decode()

print(type(idm))
print(place_id)

data = {
    "user_name":idm,
    "place_id":place_id
}

requests.post("http://127.0.0.1:8000/api",data)

# b'01010310f309530e'
print('please released card')
