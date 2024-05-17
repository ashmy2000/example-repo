data = bytearray(100)
data[0] = 100
data[1] = 120

try:
    stream = open("file.bin", "wb")
    stream.write(data)
    stream.close()
except Exception as e:
    print(e)

try:
    bf = open("file.bin", "rb")
    byte_Array = bf.read()
    for byte in byte_Array:
        print(int(byte), end=" ")
    bf.close()
except Exception as e:
    print(e)

# print(byte_Array)
# for byte in byte_Array:
#     print(hex(byte), end="")
