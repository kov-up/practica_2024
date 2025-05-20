a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
    if a > c:	
        print('a - max')
elif b > c:	
    print('b - max')
else:
    print('c - max')
print('min + max = ', max(a,b,c) + min(a,b,c))
print(min(a, b, c))
print(max(a, b, c))

