#Duvall Pinkney
#3/15/2015
#due date 3/16/2015---- program number 20 homwwork

def main():
    stringOfNames = input("Please enter your list of names: ")
    name1, name2, name3, name4, name5 = stringOfNames.split(';')
    
    lName1,fName1 = name1.split(',')
    lName2,fName2 = name2.split(',')
    lName3,fName3 = name3.split(',')
    lName4,fName4 = name4.split(',')
    lName5,fName5 = name5.split(',')
    
    
    print("You entered: ")
    print("")
    print(fName1,lName1)
    print(fName2,lName2)
    print(fName3,lName3)
    print(fName4,lName4)
    print(fName5,lName5)
    print("")
    print("Thank you for using my name organizer!")

main()    
