with open('binary.bin', 'wb') as f:
    f.write(b'\xea\xbo\x80')

input()
with open('text.bin', 'r', encoding='utf-8') as f:
    data = f.read()
print(data)