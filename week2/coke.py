due=50
print(f'Amount due: {due}')
while due>0:
    coin=input('Insert coin: ')
    match coin:
        case '25':
            due=due-25
            if due>0:
                print(f'Amount Due: {due}')
        case '10':
            due=due-10
            if due>0:
                print(f'Amount Due: {due}')
        case '5':
            due=due-5
            if due>0:
                print(f'Amount Due: {due}')
        case _:
            print(f'Amount Due: {due}')
print(f'Change Owed: {due.__abs__()}')
