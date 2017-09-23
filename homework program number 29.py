#Duvall Pinkney
#3/28/2015
#homework program number 29


def getGrades():
    filename = input("please enter filename: ")
    infile = open(filename, "r")
        
    for line in enumerate(infile):
        grades = infile.readline()
            
            
        
            
    return grades

def calculateAverage(grades):
    counter = 0
    total = 0
    for i in grades:
        grades = grades.split(",")
            

        for numstr in range(grades):
            counter = counter + 1
            total = total + float(numstr)
    return (total/counter)        
            
            
        
            
def main():       

    grades = getGrades()



    avg = calculateAverage(grades)



    print("The calculated average is:", avg)
main()    
