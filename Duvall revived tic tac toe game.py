# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 05:06:39 2018

@author: Duvall Pinkney
         Duvall.Pinkney@gmail.com
"""

#Duvall Pinkney
#12/8/2018


from turtle  import *

def drawGrid():
    #initialize ninja turtle
    #win = Screen()
    ninja = Turtle()
    ninja.shape('turtle')
    
    
    # draw grid-------300 x 300 box
    # 100 pixels x 100 pixels box with center at (x -50,y-50) pixels
    #point(0,0) starting
    ninja.up()
    ninja.forward(150)
    ninja.left(90)
    ninja.down()
    ninja.forward(150)
    
    ninja.left(90)
    #point(150,150) pixels
    
    ninja.forward(300)
    #point(-150,150)
    
    ninja.left(90)
    ninja.forward(300)
    #point(-150,-150)
    ninja.left(90)
    ninja.forward(300)
    #point(150,-150)
    ninja.left(90)
    ninja.forward(300)
    #point(150,150)
    
    ninja.up()
    ninja.left(90)
    ninja.forward(100)
    #point(50,150)
    ninja.left(90)
    ninja.down()
    ninja.forward(300)
    #point(50,-150)
    ninja.right(90)
    ninja.up()
    ninja.forward(100)
    #point(-50,-150)
    ninja.right(90)
    ninja.down()
    ninja.forward(300)
    #point(50,150)
    ninja.up()
    ninja.left(90)
    ninja.forward(100)
    ninja.left(90)
    ninja.forward(100)
    ninja.left(90)
    ninja.down()
    ninja.forward(300)
    ninja.up()
    ninja.right(90)
    ninja.forward(100)
    ninja.right(90)
    ninja.down()
    ninja.forward(300)
    
    
    
    
#    #-------------------------initialize values-------------------------
    def winconditions:
        
        
    
    #decide by random who goes first X or O
    
    def chooseWhoGoesFirst():
        
    
    #create gamplay loop with win conditions
    def GamePlay():
        
        drawGrid()
        #enlarge value or X and O and print fill in grid color with blue or 
        #red X or O
        while (numberOfturns <= 9):
            #game vi
            if (topLeftGrid && centerLeftGrid && bottomLeftGrid = "X"):
                print("player X wins")
                break
            elif (topLeftGrid && centerLeftGrid && bottomLeftGrid = "O"):
                print("player O wins")
                break
            elif (topCenterGrid && centerGrid && bottomCenterGrid = "X"):
                print("player X wins")
                break
            elif (topCenterGrid && centerGrid && bottomCenterGrid = "O"):
                print("player O wins")
                break
            elif (topRightGrid && centerRightGrid && bottomRightGrid = "X"):
                print("player X wins")
                break
            elif (topRightGrid && centerRightGrid && bottomRightGrid = "O"):
                print("player O wins")
                break
            elif (topLeftGrid && topCenterGrid && topRightGrid = "X"):
                print("player X wins")
                break
            elif (topLeftGrid && topCenterGrid && topRightGrid = "O"):
                print("player O wins")
                break
            elif (centerLeftGrid && centerGrid && centerRightGrid = "X"):
                print("player X wins")
                break
            elif (centerLeftGrid && centerGrid && centerRightGrid = "O"):
                print("player O wins")
                break
            elif (bottomLeftGrid && bottomCenterGrid && bottomRightGrid = "X"):
                print("player X wins")
                break
            elif (bottomLeftGrid && bottomCenterGrid && bottomRightGrid = "O"):
                print("player O wins")
                break
            elif (topLeftGrid && centerGrid && bottomRightGrid = "X"):
                print("player X wins")
                break
            elif (topLeftGrid && centerGrid && bottomRightGrid = "O"):
                print("player O wins")
                break
            elif ( topRightGrid && centerGrid && bottomLeftGrid = "X"):
                print("player X wins")
                break
            elif ( topRightGrid && centerGrid && bottomLeftGrid = "O"):
                print("player O wins")
                break
            else:
                print("it is a draw")
                break
        #get user input
   
        
    
    # create X controls so that if grid is  filled you can not select it
    def Xcontrols(xValue):
        xValue = this.xValue;
        value = xValue;
            #----------------In game controls/methods-------------------------------
        def topleft(value):
            xOutput = -100
            yOutput = 100
            ninja.goto(xOutput, yOutput)
            if (topLeftGrid == ""):
                ninja.write(value)
            elif (topLeftGrid == "O"):
                print("You can not write to this grid choose another")
                #insert function call to choosing a grid
            
            
            
            #object storing value for win conditions
            # X or O
            topLeftGrid = value
        
            
        def centerleft(value):
            xOutput = -100
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            centerLeftGrid = value
            
        def bottomleft(value):
            xOutput = -100
            yOutput = -100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            bottomLeftGrid = value
            
        def topcenter(value):    
            xOutput = 0
            yOutput = 100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            topCenterGrid = value
            
        def center(value):
            xOutput = 0
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            centerGrid = value
            
            
        def bottomcenter(value):
            xOutput = -100
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            bottomCenterGrid = value
            
        def topright(value):
            xOutput = 100
            yOutput = 100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            topRightGrid = value
            
            
        def centerright(value):
            xOutput = 100
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            centerRightGrid = value
            
        def bottomright(value):
            xOutput = 100
            yOutput = -100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            bottomRightGrid = value
    
    
    #create O controls so that if grid is filled you can not select it
    def Ocontrols( oValue ):
        oValue = this.oValue;
        value = oValue;
            #----------------In game controls/methods-------------------------------
        def topleft(value):
            xOutput = -100
            yOutput = 100
            ninja.goto(xOutput, yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            # X or O
            topLeftGrid = value
            
        def centerleft(value):
            xOutput = -100
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            centerLeftGrid = value
            
        def bottomleft(value):
            xOutput = -100
            yOutput = -100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            bottomLeftGrid = value
            
        def topcenter(value):    
            xOutput = 0
            yOutput = 100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            topCenterGrid = value
            
        def center(value):
            xOutput = 0
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            centerGrid = value
            
            
        def bottomcenter(value):
            xOutput = -100
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            bottomCenterGrid = value
            
        def topright(value):
            xOutput = 100
            yOutput = 100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            topRightGrid = value
            
            
        def centerright(value):
            xOutput = 100
            yOutput = 0
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            centerRightGrid = value
            
        def bottomright(value):
            xOutput = 100
            yOutput = -100
            ninja.goto(xOutput,yOutput)
            ninja.write(value)
            
            #object storing value for win conditions
            bottomRightGrid = value
            
    
    
    
    
    #--------------------end grid construction---------------------------------
    
    
    #coordinates of the center of each 100 x 100 grid
    #----------------In game controls/methods-------------------------------
    def topleft(value):
        xOutput = -100
        yOutput = 100
        ninja.goto(xOutput, yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        # X or O
        topLeftGrid = value
        
    def centerleft(value):
        xOutput = -100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerLeftGrid = value
        
    def bottomleft(value):
        xOutput = -100
        yOutput = -100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomLeftGrid = value
        
    def topcenter(value):    
        xOutput = 0
        yOutput = 100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        topCenterGrid = value
        
    def center(value):
        xOutput = 0
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerGrid = value
        
        
    def bottomcenter(value):
        xOutput = -100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomCenterGrid = value
        
    def topright(value):
        xOutput = 100
        yOutput = 100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        topRightGrid = value
        
        
    def centerright(value):
        xOutput = 100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerRightGrid = value
        
    def bottomright(value):
        xOutput = 100
        yOutput = -100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomRightGrid = value
        
        
        
        
        
    


gameplay()