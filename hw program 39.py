#Duvall pinkney
#4/19/2015
#hw program number 39

##Due Date: 21 April Reading: Chapter 7
##Define a Python function named calculate_tax() which accepts one parameter,
##income, and returns the income tax. Income is taxed according to the following
##rule: the first $250,000 is taxed at 40% and any remaining income is taxed at
##80%. For example, calculate_tax(100000) should
##return $100,000 * 0.40 = $40,000, while calculate_tax(300000) should
####return $250,000 * 0.40 + 50,000 * 0.80 = $140,000.


def calculate_tax(income):
    remainIncome = income - 250000
    if income >= 250000:
        if remainIncome < 0:
           return income * 0.40
        if remainIncome > 0:
            
           return income * 0.40 + (remainIncome * 0.80)
    
    if income <= 100000:
       return income * 0.40


def main():
    income = eval(input("Please enter your income: "))
    
    print(calculate_tax(income))



main()    
    
