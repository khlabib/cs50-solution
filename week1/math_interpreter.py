x,y,z=input('Expression :').strip().split()
match y:
    case '+':
        print('{0:.1f}'.format(float(x)+float(z)))
    case '-':
        print('{0:.1f}'.format(float(x)-float(z)))
    case '*':
        print('{0:.1f}'.format(float(x)*float(z)))
    case '/':
        print('{0:.1f}'.format(float(x)/float(z)))
    case _:
        print('invalid input')