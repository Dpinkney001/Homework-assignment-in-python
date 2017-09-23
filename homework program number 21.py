#Duvall Pinkney
#Due:3/17/2015
#homework program number 21

def main():
    filename = input("Please enter your file name: ")
    infile = open(filename,"r")
    info = infile.read()
    print("")
    print("")
    print("Your file in upper case letters is: ")
    print(info)

main()    
