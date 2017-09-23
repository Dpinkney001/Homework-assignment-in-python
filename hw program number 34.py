#Duvall Pinkney
#4/4/2015
#hw program number34

def square():
    num1,num2,num3,num4,num5 = eval(input("Enter a list of 5 numbers separated by a comma: "))
    listOfNums = [num1, num2, num3, num4, num5]
    num1 = num1 ** 2
    num2 = num2 ** 2 
    num3 = num3 ** 2
    num4 = num4 ** 2
    num5 = num5 ** 2


    
        #enum[num] = nums[num]
        #hile num >= 0:
         #   enum[num] = enum ** 2
          #  num = num - 1



    return num1, num2, num3, num4, num5
def main():
    
    print(square())    
main()
