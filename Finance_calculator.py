import math                                                                                   #use the import math function


print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")              #display the two options available for calculation
print("Investment   - to calculate the amount of interest you'll earn on interest ")          #option 1 - interest earned on an investment
print("Bond         - to calculate the amount you'll have to pay on a home loan \n")          #option 2 - monthly bond repayments on a home loan


choice = input("Enter your choice: ")                                                         #user makes a choice
                                                                                              #input can be upper case or lower case characters








#investment calculation
if choice.lower() == "investment" or choice.upper() == "investment":                           
    P = float(input("Input the amount you woule like to deposit: "))                           #request amount deposited
    R = float(input("Input the interest rate you would like to receive: "))/100                #request interest rate and divide by 100
    T = float(input("Input the number of the number of years you're investing for: "))         #request investment period
    interest = input("Do you want simple or compound interest applied? ")                      # request the type of interest to be received
    

# simple interest calculation
    SI = P*(1+R*T)                                                                            #SI = SIMPLE INTEREST
    if interest =="simple":
        print("Your total investment will be R ", SI)

#coumpond interest calculation
    CI = P*(math.pow((1+R),T))                                                                #CI= COMPOUND INTEREST                                            
    if interest == "compound":
        print("Your total investment will be R ", CI)






#bond calculation
if choice.lower() or choice.upper() == "bond":
    PV = float(input("Input the present value of your house: "))
    R = float(input("Input the interest rate you want to pay: "))/100
    N = float(input("Input the number of pay off years you wish to repay your bond: "))
    repayment = PV*(math.pow((1+R/12), N))
    print("Your total is R ", repayment)



  
    


    

    


