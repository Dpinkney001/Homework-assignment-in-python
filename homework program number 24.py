#Duvall Pinkney
#Due: 3/20/2015
#homework program number 24

def main():
    filename = input("Please enter your file name: ")
    infile = open(filename,"r")
    
    
    

    def readshit():
        data1 = infile.readline()
        data2 = infile.readline()
        data3 = infile.readline()
        data4 = infile.readline()
        data5 = infile.readline()

        data1 = eval(data1)
        data2 = eval(data2)
        data3 = eval(data3)
        data4 = eval(data4)
        
        
        sumOfNums = data1 + data2 + data3 + data4
        return(sumOfNums)

    print("The sum of your numbers is",readshit())     



main()        
