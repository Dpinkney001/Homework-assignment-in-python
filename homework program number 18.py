#Duvall Pinkney
#3/11/2015
#program number 18

def main():
    s = input("Please enter a string of text: ")
    l = len(s)
    for i in range(0,l-1):
        print(s[0:i])
    for i in range(0,l-1):
        print(s[i:l])

    print("The end")     

main()
