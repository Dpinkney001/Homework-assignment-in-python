#duvall Pinkney
#5/4/2015
#hw program number 46



####Write a program that will take earthquake data from the US Geological Survey and map it
##to the screen. The data files are spreadsheets stored in "comma separated values" (CSV) format.
##For example, here are the first couple of lines of the file of all earthquakes from the week of 13 March 2015:
####time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place,type
####2015-03-20T10:20:35.890Z,38.8221664,-122.7649994,2.48,0.92,md,15,52,0.009138,0.04,nc,nc72414375,
##    2015-03-20T10:35:05.263Z,"3km W of Cobb, California",earthquake
####2015-03-20T10:18:13.070Z,33.2073333,-116.6891667,8.65,0.6,ml,15,92,0.03606,0.12,ci,ci37343784,2015-03-20T10:22:09.236Z,
##    "8km ESE of Lake Henshaw, California",earthquake
####2015-03-20T10:15:09.000Z,62.242,-150.8769,58.2,1.5,ml,,,,0.51,ak,ak11532412,2015-03-20T10:26:23.671Z,
##    "40km WSW of Talkeetna, Alaska",earthquake
####The first line describes the columns and the remaining lines are the actual data about earthquakes.
##    To map a quake, we need to know its location which is stored in the latitude and longitude columns. For example, if line is a
#line of the file, then the location of the earthquake is (x,y) where:
####	cells = line.split(",")
####	y = cells[1]
####	x = cells[2]


from turtle import *

def setUpScreen():
     w = turtle.Screen()
     w.setworldcoordinates(-181,-91,181,91)
     return(w)

def drawOceans():
     infile = open("dayAll_2015Mar18.csv","r")#A file with coordinates field only
     lines = infile.readlines()         #Read in the lines of the file
     tracy = turtle.Turtle()
     tracy.speed(10)

     for line in lines:                
          start = line.find("[[[")+1    #Find where the coordinates start
          end = line.find("]]]}")+2     #    and ends
          coordString = line[start:end] #Grab the coordinates, ignoring last 5 characters in line
                                        #    (not needed in our format)
          coordinates = eval(coordString)    #Turn the string into list of numbers
          print(coordinates[-1])
          tracy.up()                   #Move to starting point without drawing
          tracy.goto(coordinates[0][0], coordinates[0][1])
          tracy.down()
          #print coordinates
          for point in coordinates:     #For each point in the list of coordinates
               print(point)
               x = point[0]             #Find the x and y of point
               y = point[1]
               tracy.goto(x,y)          #Move the turtle to the (x,y)


def getQuakeData():
     #Fill in this function definition!#
    infile = open("dayAll_2015Mar18.csv",'r')
    
     print("\n\nTO BE IMPLEMENTED:")
     print("This function gets data from file")

def drawQuakes(lines):
     #Fill in this function definition!#
     print("\n\nTO BE IMPLEMENTED:")     
     print("This function parses lines and stamps at quake locations")
     
def main():
     w = setUpScreen()   #Set up the screen with lower left (-90,-180) and upper right (90,180)
     drawOceans()        #Draws oceans using the oceansSimplified.json file
     lines = getQuakeData()   #Asks user for quake file and returns list of lines
     drawQuakes(lines)   #Stamps at each point in each line
     w.exitonclick()     #Close the window when clicked

main()
