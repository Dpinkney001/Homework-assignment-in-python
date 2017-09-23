#Duvall Pinkney
#4/17/2015
#program number 38

def bus(zone,ticketType):
    counter = 0
    fare = 0.0
    
                
    if zone <= 2  and ticketType == "adult":
        fare = 23
        counter + 1
        return fare
    if zone <= 2  and ticketType == "child":
        fare = 11.5
        counter + 1
        return fare
    if zone == 3 and ticketType == "adult":
        fare = 34.5
        counter + 1
        return fare
    if zone == 3 or zone == 4 and ticketType == "child":
        fare = 23
        counter + 1 
        return fare
    if zone == 4 and ticketType == "adult":
        fare = 46
        counter + 1 
        return fare
    if zone > 4:
        return -1
    for i in range(counter):
        CopenhagenTransitFare = fare + fare
        return CopenhagenTransitFare
                

                

def main():
    zone = eval(input("please enter zone: "))
    ticketType = input("enter child or adult: ")


    
    bus(zone,ticketType)
    bus(zone,ticketType)
    bus(zone,ticketType)
    bus(zone,ticketType)
    bus(zone,ticketType)
    bus(zone,ticketType)
    bus(zone,ticketType)
    bus(zone,ticketType)
    bus(zone,ticketType)

    print(bus(zone,ticketType))
main()    

##Write a function that takes as two parameters: the zone and the ticket type, and returns the Copenhagen Transit fare.
##If the zone is 2 or smaller and the ticket type is "adult", the fare is 23.
##If the zone is 2 or smaller and the ticket type is "child", the fare is 11.5.
##If the zone is 3 and the ticket type is "adult", the fare is 34.5.
##If the zone is 3 or 4 and the ticket type is "child", the fare is 23.
##If the zone is 4 and the ticket type is "adult", the fare is 46.
##If the zone is greater than 4, return a negative number (since your calculator does not handle inputs that high).
##You should include in the file a main() that calls your function several times to demonstrate that it works.
