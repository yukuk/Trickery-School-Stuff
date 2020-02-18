st = input()
kol = int('X' in st) + int('Y' in st) + int('Z' in st) + int('W' in st)
letters = "XYZW"
for i in range(kol):
    print(letters[i], end='\t')
print('F')
i_ = 0
for i in range(2 ** kol):
    i_ = i
    X = i_ // (2 ** (kol - 1))
    i_ %= 2 ** (kol - 1)
    Y = i_ // (2 ** (kol - 2))
    i_ %= 2 ** (kol - 2)
    Z = i_ // (2 ** (kol - 3))
    i_ %= 2 ** (kol - 3)
    W = i_ // (2 ** (kol - 4))
    i_ %= 2 ** (kol - 4)
    if 'X' in st:
        print(X, end='\t')
    if 'Y' in st:
        print(Y, end='\t')
    if 'Z' in st:
        print(Z, end='\t')
    if 'W' in st:
        print(W, end='\t')
    print(int(eval(st)))