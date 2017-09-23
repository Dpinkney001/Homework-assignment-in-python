#Duvall Pinkney
#due date 3/23/2015
#homework program number 25

def main():
    filename = input("Please enter your filename: ")
    infile = open(filename,"r")


    def readandcount():
        data1 = infile.readline()
        data1, data2 = data1.split(',')
        data3 = infile.readline()
        data4 = infile.readline()
        data4,data5, data6, data7 = data4.split(',') 
        data8 = infile.readline()

        float(data1)
        float(data2)
        float(data4)
        float(data5)
        float(data6)
        float(data7)
        float(data3)
        float(data8)
        contentsAdded = data1 + data2 + data3 + data4 + data5 + data6 +data7 + data8
        
        
        line1data = eval(contentsAdded)
        
        
        
         
        return(line1data)
    print("The sum of your numbers is ",readandcount(),".")

main()    
