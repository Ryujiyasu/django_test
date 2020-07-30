import nfc
import binascii
import requests
import random


clf = nfc.ContactlessFrontend('usb')
print('カードを置いてください：')
try:
    tag = clf.connect(rdwr={'on-connect': lambda tag: False})
finally:
    clf.close()

# b'01010310f309530e'
idm = binascii.hexlify(tag.idm)

# 場所を「1～3」の中からランダムに選択
place_id = random.randint(1, 3)

# バイナリ型を文字列型へ変換
idm = idm.decode()

# カードから読み取った情報を送信用の辞書型へ格納
data = {
    "user_name": idm,
    "place_id": place_id
}

# カードから読み取った情報を送信
result = ""
result = requests.post("http://127.0.0.1:8000/api", data)

print(result)
print("カードを離してください")
