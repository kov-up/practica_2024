a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > b:
    if a > c:	
        print('a - maximum')
elif b > c:	
    print('b - maximum')
else:
    print('c - maximum')
print('min + max = ', max(a,b,c) + min(a,b,c))
print(min(a, b, c))
print(max(a, b, c))

