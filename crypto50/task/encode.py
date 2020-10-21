import random as rnd

flag = '<redacted>'
f = int.from_bytes(bytes(flag.encode('ascii')), 'big')
B = len(bin(f))
print(B)
p = 0
for i in range(1000):
    p += 2 ** i * rnd.randint(0, 1)
print(p)
n = p ** 17
out = open('output.txt', 'w')
out.write(str(n) + '\n' + str((p ^ f)) + '\n')
out.close()
