#Duvall Pinkney
#4/21/2015
#hw program number 40

##Due Date: 22 April Reading: Chapter 7
##Write a function that takes a list of strings and returns the number of strings longer than 10 characters in the inputted list .
##You should include in the file a main() that calls your function several times to demonstrate that it works.

def stringsFunction():
    
    Lst = ["obelisk the tormentor" ,"The winged dragon of Ra","Sylifer the sky dragon"]
    outLst = []
    counter = 0
    for item in Lst:
        outLst.append(len(item))
    
        if  len(item) > 10:
            counter = counter + 1
            return counter
    
    
def main():


    print("The number of strings in the list with length greater thant 10 are ",stringsFunction())
    




main()



