with open('binary_to_test.bin', 'wb') as f:
    ga = b'\xea\xb0\x80'
    f.write(ga)

with open('binary_to_test.bin', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)