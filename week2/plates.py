import sys
#main function

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#user defined function to check validity of plate

def is_valid(s):

    digitcounter = 0
    firstzero = 0
    return_value = 0

    #condition maximum character limit 6 and minimum 2
    #there is no else for the following if, so the second condition is also satisfied

    def first(a):
        return_value = 0

        for c in a[:2]:
            #check if character is letter
            if c.isalpha():
                return_value += 1
            else:
                return_value = 0
                break
        return return_value


    def second(b):
        if 2 <= len(b) <= 6:
            return True
        else:
            return False
        #loop for first two characters

        #by this line, the first conditon is satisfied
        #loop for characters except first two

        ####


    def third(c):
        firstzero = 0
        return_value = 0

        for i in c[2:]:
            #check if character is digit
            if i.isdigit():
                #check if character is zero
                if int(i)==0:
                    #if the following if is true, that takes us out of the for loop
                    #firstzero detects if it is first zero, digitcounter detects if it is first digit
                    #if the following is true, means it is the first appearance of digit, and is zero
                    if firstzero == 0:
                        #print('compiler is here')
                        firstzero=1
                        return False
            #by this line, the character is zero, but not the first zero
            #if character is not zero
            #regardless of the first being zero or not, digitcounter must be updated as it
            # indicates the first appearance of a digit
                firstzero = 1
        #first condition check if there was a digit before this character and current character is letter
        #second condition checks if current character is a special character
        #both works in conjunction with OR
        #the following if checks for both condition 3 and 4
            if (firstzero == 1 and i.isalpha()):
                return False
            else:
                return_value = 1
        return return_value


    def fourth(d):
        for i in d[2:]:
            if (not i.isalpha() and not i.isdigit()):
                return False
        return True

    if first(s) and second(s) and third(s) and fourth(s):
        return True


#main function call
if __name__ == "__main__":
    main()