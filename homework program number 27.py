#Duvall Pinkney
#Due date: 3/25/2015
#homework program number#27

def main():
    infilename = input("Please enter filename: ")
    outfilename = input("Please enter output file name: ")

    infile = open(infilename,"r")
    outfile = open(outfilename,"w")
    
    for line,data in enumerate(infile):
        
        print(line+1,data,'\t', file=outfile)

    infile.close()
    outfile.close()
main()

    
