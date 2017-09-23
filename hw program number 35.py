#Duvall Pinkney
#4/5/2015
#hw program number 35



from turtle import *

def main():
    win = Screen()
    duvall = Turtle()
    duvall.shape('turtle')
    duvall.down()
    
    
    sizeOfGrid = eval(input("Please enter the size of the grid: ")
    
    duvall.forward(sizeOfGrid)
    duvall.left(90)
    duvall.forward(sizeOfGrid)
    duvall.left(90)
    duvall.forward(sizeOfGrid)
    duvall.left(90)
    duvall.forwards(sizeOfGrid)
                      
                      
    
        
##    for i in range(0,62,2)
##        row = i // sizeOfGrid
##        offset = row % 2
##        col = (i % sizeOfGrid) + offset              
##    


main()
###1.  Ask the user for the size of the checkered flag (n).
##2.  Draw an n x n grid to the screen.
##3.  For i = 0,2,4,...,62:
##4.     row = i // n
##5.     offset = row % 2
##6.     col = (i % n) + offset
