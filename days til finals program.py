#Duvall Pinkney
#2/8/2015
#program number 6-Due 2/18/2015
# this program calculates the number weeks and days left til the final
# exam based on the number of days the use inputs

def FinalDays():
    print("Please enter the number of days until finals:->  ")
    finaldays = eval(input(" "))
    weeks = finaldays / 7
    remains = finaldays % 7
    print("There are ")
    print(weeks)
    print(" week(s) til finals. ")
    print("and ")
    print(remains)
    print(" day(s) remaining.")

FinalDays()
    
