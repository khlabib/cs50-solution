#a main function that takes input from user and calls the user defined function
def main():
    original=input()
    convert(original)

#an user defined function that takes a string and returns coverted emoticons
def convert(to):
    converted=to.replace(':)','\N{slightly smiling face}').replace(':(','\N{slightly frowning face}')
    print(converted)

#call main function
main()
