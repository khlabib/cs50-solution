camel=input('camelCase : ')
for c in camel:
    if c.isupper():
        print('_',end='')
        c=c.lower()
    print(c,end='')
print('')