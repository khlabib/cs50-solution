initial=input('Input: ')
print('Output: ',end='')
for c in initial:
    if (c=='a' or c=='A' or c=='e' or c=='E' or c=='i' or c=='I' or c=='o' or c=='O' or c=='u' or c=='U'):
        continue
    else:
        print(c,end='')
print()

