a = 1
b = 2
c = a + b

sum = 2
while True:
    if c < 4000000:
        c = a + b
    else:
        break
    if c % 2 == 0:
        sum += c
    a = b
    b = c

print(sum)
