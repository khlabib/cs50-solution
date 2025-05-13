def main():
    #get time
    answer=input('What time is it?')
    #call convert function
    ftime=convert(answer)
    #if time between 7 and 8
    if 7<=ftime<=8:
        print('Breakfast time')
    #if time between 12 and 13
    elif 12<=ftime<=13:
        print('Lunch time')
    #if time between 18 and 19
    elif 18<=ftime<=19:
        print('Dinner time')
def convert(time):
    #split into hours and minutes
    hours,minutes=time.split(':')
    #convert 7:30 into 7.5
    new_minutes=float(minutes) /60
    #return new time
    return float(hours)+new_minutes

if __name__ == "__main__":
    main()