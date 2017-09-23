#Duvall Pinkney
#4/17/2015
#program number 37


######Write a function that takes number between 1 and 7 as a parameter and returns out the corresponding day as a string.
##For example, if the parameter is 1, your function should return out one. If the parameter is 2, your function should return out two,
##etc.
####In your file, you should include a main() that allows the user to enter a number and calls your function to demonstrate that it
##works.

def someFunction(num):
     
     if num == 1:
         
         return "one"
     if num == 2:
         
         return  "two"
     if num == 3:
         
         return "three"
     if num == 4:
         
         return  "four"
     if num == 5:
         
         return  "five"
     if num == 6:
         
         return  "six"
     if num == 7:
         
         return  "seven"

    
     


def main():
    
    num = eval(input("Please enter a number from one through seven: "))

    

    someFunction(num)
    print(someFunction(num))
     




main()
