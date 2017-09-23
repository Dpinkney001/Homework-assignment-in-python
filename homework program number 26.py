#Duvall Pinkney
#due3/24/2015
#homework program number 26

def main():
    filename = input("Please enter  a file name: ")
    outputfilename = input(" Please enter the name of the output file: ")
    
    infile = open(filename,"r")
    outfile = open(outputfilename, "w")
    for lines in infile:
        data = infile.read()
        print(data, file=outfile)
        newdata = data.replace( "NY","New York")
        

        for lines in infile:
            newdata = infile.read()
            print(newdata, file=outfile) 
            newdata2 = data2.replace( "NJ", "New Jersey")

            for lines in infile:
                newdata2 = infile.read()
                print(newdata2, file=outfile)
                newdata3 = data3.replace("CT", "Connecticut")
                print(newdata3, file=outfile)


main()
