#Duvall Pinkney
#4/5/2015
#hw program number 35



from turtle import *

def setUpScreen(xMax,yMax):
    xMax,yMax = eval(input("Please enter the size of the grid(length,width): "))
    win = Screen()
    win.setworldcoordinates(-0.5, yMax+0.5,xMax+0.5,-0.5)
    return win
    

def drawGrid(xMax,yMax):
    ninja = Turtle()
    ninja.speed(10)
    #Draw the vertical bars of the game board:
    for i in range(0,xMax+1):
        ninja.up()
        ninja.goto(0,i)
        ninja.down()
        ninja.forward(yMax)

    #Draw the horizontal bars of the game board:
    ninja.left(90)    #Point the turtle in the right direction before drawing
    for i in range(0,yMax+1):
        ninja.up()
        ninja.goto(i,0)
        ninja.down()
        ninja.forward(xMax)


def main():
    
    
##    1.  Ask the user for the size of the checkered flag (n).
##2.  Draw an n x n grid to the screen.
##3.  For i = 0,2,4,...,n*n-1:
##4.     row = i // n
##5.     offset = row % 2
##6.     col = (i % n) + offset
##7.     fillSquare(row,col,"black")
    
    
##    for i in range(0,62,2):
##        row = i // n
##        offset = row % 2
##        col = (i % n) + offset
    setUpScreen(xMax,yMax)
    drawGrid(xMax,yMax)

####    ninja.forward(n)
####    ninja.left(90)
####    ninja.forward(n)
####    ninja.left(90)
####    ninja.forward(n)
####    ninja.left(90)
####    ninja.forward(n)
####    ninja.left(90)
####    
##        ninja.forward(offset)
##        ninja.left(90)
##        ninja.forward(offset)
####        for r in range(row):
##            
##            ninja.down()
##            ninja.forward(row)
##            ninja.left(90)
##            ninja.forward(row)
##            ninja.left(90)
##            ninja.forward(row)
##            ninja.left(90)
##            ninja.forward(row)
##            ninja.up()
##
##            ninja.goto()

##       ninja.down()
##       
##        
##        ninja.forward(row)
##        ninja.left(90)
##        ninja.forward(row)
##        ninja.left(90)
##        ninja.forward(row)
##        ninja.left(90)
##        ninja.forward(row)
##
##        ninja.forward(col)
##        ninja.left(90)
##        ninja.forward(col)
##        ninja.left(90)
##        ninja.forward(col)
##        ninja.left(90)
##        ninja.forward(col)
##
##        ninja.forward(offset)
##        ninja.left(90)
##        ninja.forward(offset)
##        ninja.left(90)
##        ninja.forward(offset)
##        ninja.left(90)
##        ninja.forward(offset)
##                       
        
                      
                      
    
        
##  


main()
###1.  Ask the user for the size of the checkered flag (n).
##2.  Draw an n x n grid to the screen.
##3.  For i = 0,2,4,...,62:
##4.     row = i // n
##5.     offset = row % 2
##6.     col = (i % n) + offset
