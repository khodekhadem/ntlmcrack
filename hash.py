import hashlib,binascii

myhash = "b'"+" hash ro in ja bezar هش رو اینجا بزار  "+"'"
myhash = myhash.lower()

file = open("adres pasword list اسم و ادرس پسورد لیست رو اینجا بزار","r")

for line in file.readlines():
    line =  line[ : len(line) - 1 ]

    hash = hashlib.new('md4', line.encode('utf-16le')).digest()
    hash = str(binascii.hexlify(hash))
    if myhash == hash:
        print(line)


