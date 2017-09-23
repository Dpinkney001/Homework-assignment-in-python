#DUvall Pinkney
#date: 3/31/2015
#homework program number 30

def sumRow(nums[row]):
    #return the sume of inputed list
    row1 = 4 + 3 + 2 + 1
    row2 = 8 + 7 + 6 + 5
    row3 = 12 + 11 + 10 + 9
    row4 = 16 + 15 + 14 + 13
    row5 = 20 + 19 + 18 + 17
    return(nums[row])






def display():
    
    
    






def main():
    wn = Screen()
    nums = [[4,3,21],
            [8,7,6,5],
            [12,11,10,9],
            [16,15,14,13],
            [20,19,18,17]]
    n = len(nums)
    m = len(nums[0])
    wn.setworldcoordinates(-0.5,n-0.5,m+2,-1.0)

    for row in range(n):
        rowTotal = sumRow(nums[row])  #returns the sum of inputted list
        for col in range(n):
            display(nums[row][col], col, row) #displays entry at (col,row)
        display("=", col+1, row)
        display(rowTotal, col+2, row)

    wn.exitonclick() # cloes the graphics window when mouse is clicked
main()    
