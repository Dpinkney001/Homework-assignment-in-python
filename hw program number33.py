#Duvall Pinkney
#4/2/2015
#hwprogram number 33
    
def food():

    string1, string2, string3, string4, string5 = input("Please enter 5 strings separated by a comma: ")

    foodstrings = [string1, string2, string3, string4, string5]

    #take the element in each array and pass it to a string var
##    string1 = foodstrings[0]
##    string2 = foodstrings[1] 
##    string3 = foodstrings[2] 
##    string4 = foodstrings[3] 
##    string5 = foodstrings[4]

    #split the list
##    string1 = string1.split(',')
##    string2 = string2.split(',')
##    string3 = string3.split(',')
##    string4 = string4.split(',')
##    string5 = string5.split(',')
 

    #edit the string var and cap it
    string1 = string1.capitalize()
    string2 = string2.capitalize()
    string3 = string3.capitalize()
    string4 = string4.capitalize()
    string5 = string5.capitalize()

    # return the edit
    return string1, string2, string3, string4, string5    
    

def main():
    #call the food string
    

    
    print(food())



main()    
