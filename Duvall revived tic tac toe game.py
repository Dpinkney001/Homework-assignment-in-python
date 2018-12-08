# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 05:06:39 2018

@author: Duvall Pinkney
         Duvall.Pinkney@gmail.com
"""

#Duvall Pinkney
#12/8/2018


from Turtle  import *

def main():
    #initialize ninja turtle
    #win = Screen()
    ninja = Turtle()
    ninja.shape('turtle')
    
    
    # draw grid-------300 x 300 box
    # 100 pixels x 100 pixels box with center at (x -50,y-50) pixels
    #point(0,0) starting
    ninja.forward(150)
    ninja.left(90)
    ninja.forward(150)
    ninja.down()
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
    
#    #-------------------------initialize values-------------------------
#    String value
#    
#    
#    #decide by random who goes first X or O
#    
#    def chooseWhoGoesFirst():
#        
#    
#    #create gamplay loop with win conditions
#    def GamePlay():
#        #enlarge value or X and O and print fill in grid color with blue or 
#        #red X or O
#        
#        #get user input
#    x,y = eval(input("Please enter coordinates: "))
#    neoX = x * 50 - 25
#    neoY = y * 50 - 25
#    
#    ninja.goto(neoX,neoY)
#    ninja.write("2")
#    print("Please hit the enter key to continue: ")
#    ninja.left(180)
#    if neoX >= 100:
#        neoX = neoX - 100
#        ninja.goto(neoX,neoY)
#        ninja.write("2")
#        ninja.goto(0,0)
#    else:
#        neoX = neoX - 50
#        ninja.goto(neoX,neoY)
#        ninja.write("2")
#        ninja.goto(0,0)
#        
#    
#    # create X controls so that if grid is  filled you can not select it
#    def Xcontrols(xValue):
#        xValue = this.xValue;
#        value = xValue;
#            #----------------In game controls/methods-------------------------------
#        def topleft(value):
#            xOutput = -100
#            yOutput = 100
#            ninja.goto(xOutput, yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            # X or O
#            topLeftGrid = value
#            
#        def centerleft(value):
#            xOutput = -100
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            centerLeftGrid = value
#            
#        def bottomleft(value):
#            xOutput = -100
#            yOutput = -100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            bottomLeftGrid = value
#            
#        def topcenter(value):    
#            xOutput = 0
#            yOutput = 100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            topCenterGrid = value
#            
#        def center(value):
#            xOutput = 0
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            centerGrid = value
#            
#            
#        def bottomcenter(value):
#            xOutput = -100
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            bottomCenterGrid = value
#            
#        def topright(value):
#            xOutput = 100
#            yOutput = 100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            topRightGrid = value
#            
#            
#        def centerright(value):
#            xOutput = 100
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            centerRightGrid = value
#            
#        def bottomright(value):
#            xOutput = 100
#            yOutput = -100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            bottomRightGrid = value
#    
#    
#    #create O controls so that if grid is filled you can not select it
#    def Ocontrols( oValue ):
#        oValue = this.oValue;
#        value = oValue;
#            #----------------In game controls/methods-------------------------------
#        def topleft(value):
#            xOutput = -100
#            yOutput = 100
#            ninja.goto(xOutput, yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            # X or O
#            topLeftGrid = value
#            
#        def centerleft(value):
#            xOutput = -100
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            centerLeftGrid = value
#            
#        def bottomleft(value):
#            xOutput = -100
#            yOutput = -100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            bottomLeftGrid = value
#            
#        def topcenter(value):    
#            xOutput = 0
#            yOutput = 100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            topCenterGrid = value
#            
#        def center(value):
#            xOutput = 0
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            centerGrid = value
#            
#            
#        def bottomcenter(value):
#            xOutput = -100
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            bottomCenterGrid = value
#            
#        def topright(value):
#            xOutput = 100
#            yOutput = 100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            topRightGrid = value
#            
#            
#        def centerright(value):
#            xOutput = 100
#            yOutput = 0
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            centerRightGrid = value
#            
#        def bottomright(value):
#            xOutput = 100
#            yOutput = -100
#            ninja.goto(xOutput,yOutput)
#            ninja.write(value)
#            
#            #object storing value for win conditions
#            bottomRightGrid = value
#            
#    
#    
#    
#    
#    #--------------------end grid construction---------------------------------
#    
#    
#    #coordinates of the center of each 100 x 100 grid
#    #----------------In game controls/methods-------------------------------
#    def topleft(value):
#        xOutput = -100
#        yOutput = 100
#        ninja.goto(xOutput, yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        # X or O
#        topLeftGrid = value
#        
#    def centerleft(value):
#        xOutput = -100
#        yOutput = 0
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        centerLeftGrid = value
#        
#    def bottomleft(value):
#        xOutput = -100
#        yOutput = -100
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        bottomLeftGrid = value
#        
#    def topcenter(value):    
#        xOutput = 0
#        yOutput = 100
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        topCenterGrid = value
#        
#    def center(value):
#        xOutput = 0
#        yOutput = 0
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        centerGrid = value
#        
#        
#    def bottomcenter(value):
#        xOutput = -100
#        yOutput = 0
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        bottomCenterGrid = value
#        
#    def topright(value):
#        xOutput = 100
#        yOutput = 100
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        topRightGrid = value
#        
#        
#    def centerright(value):
#        xOutput = 100
#        yOutput = 0
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        centerRightGrid = value
#        
#    def bottomright(value):
#        xOutput = 100
#        yOutput = -100
#        ninja.goto(xOutput,yOutput)
#        ninja.write(value)
#        
#        #object storing value for win conditions
#        bottomRightGrid = value
#        
#        
        
        
        
    


main()