russianwords = [b"\xd0\xb1\xd0\xbb\xd1\x8f", b"\xd0\xbf\xd0\xb8\xd0\xb7\xd0\xb4", b"\xd1\x85\xd1\x83\xd0\xb9", b"\xd0\xb5\xd0\xb1\xd0\xb0\xd1\x82\xd1\x8c", b"\xd0\xb5\xd0\xb1\xd0\xb0", b"\xd0\xbd\xd0\xb0\xd1\x85\xd1\x83", b"\xd0\xbd\xd0\xb5\xd0\xb3\xd1\x80", b"\xd1\x85\xd0\xb5\xd1\x80", b"\xd0\xb5\xd0\xb1\xd0\xbb\xd0\xb0\xd0\xbd", b"\xd0\xb4\xd0\xbe\xd0\xbb\xd0\xb1\xd0\xbe\xd1\x91\xd0\xb1", b"\xd0\xbf\xd0\xb8\xd1\x81\xd1\x8c\xd0\xba", b"\xd1\x85\xd1\x83\xd0\xb8\xd0\xbb", b"\xd0\xbf\xd0\xb8\xd0\xb4\xd0\xbe", b"\xd0\xb5\xd0\xb1\xd0\xb0\xd0\xbb", b"\xd1\x81\xd1\x83\xd0\xba\xd0\xb0"]

print('Enter text: ')
text = input()
for i in range(russianwords.__len__()):
    a = russianwords[i].decode('utf-8')
    if text.__contains__(a):
        text = text.replace(a, '*' * a.__len__())

print(text)
