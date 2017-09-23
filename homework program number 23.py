#Duvall Pinkney
#DUE date: 3/19/2015
#homework program number 23

def main():
    filename = input("Please enter your file name: ")
    infile = open(filename,"r")

    print('')
    print("The first letters of the lines in your file are:  ")
    for data in range(5):
        data = infile.readline()
        print(data[0:1])
main()        
    
