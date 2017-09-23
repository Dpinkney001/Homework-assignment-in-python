# Duvall Pinkney
# 2/7/2015
#program number 4
#program asks the user for the diameter of a circular table amd prints out the
#circumference.

def circleTable():
    print(" The program will out put the circumference of a circle table. ")
    print("Please enter the diameter of the table: ")

    #import math for pi
    import math

    diameterOfCircle = eval(input("-> "))
    circumference = diameterOfCircle * math.pi
    print(circumference)

circleTable()    
