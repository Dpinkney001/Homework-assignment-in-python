#Duvall Pinkney
#2/8/2015
#program number 5
#currency covertion program will convert american Dollar to Danish Krone (DKK)

def MoneyMoneyMoney():
    print(" This program will print out a conversion table for the American ")
    print("Dollar to the Danish Krone(DKK). ")
    print("Program written by Duvall Pinkney.")
    print("                                  ")      
    print("Dollar:   Danish Krone(DKK): ")

    #for ever 1 dollar in 5 dollars convert to danish krone and print
    for usd in range(6):

        
        conversion = usd * 5.67
        
        print(usd,"       ",conversion)
        
MoneyMoneyMoney()
        
