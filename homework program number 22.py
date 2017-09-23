#Duvall Pinkney
#due date: 3/18/2015
#homework program number 22

def main():
    filename = input("Enter file name: ")
    infile = open(filename,"r")

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()
    
    numberOfChar1 = line1.count("")
    numberOfChar2 = line2.count("")
    numberOfChar3 = line3.count("")
    numberOfChar4 = line4.count("")
    numberOfChar5 = line5.count("")

    print("")
    print("Line character count is: ",numberOfChar1)
    print("Line character count is: ",numberOfChar2)
    print("Line character count is: ",numberOfChar3)
    print("Line character count is: ",numberOfChar4)
    print("Line character count is: ",numberOfChar5)

main()
