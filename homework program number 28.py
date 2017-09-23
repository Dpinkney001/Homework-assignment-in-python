#Duvall pinkney
#Due 3/26/2015
# program number 28

from turtle import*

def main():
    myWin = turtle.Screen()
    pinkney = turtle.Turtle()
    drawStem(pinkney)
    for i in range(20):
        drawPetal(pinkney,"blue")
        drawPetal(pinkney,"purple")
    myWin.exitonclick()

main()
