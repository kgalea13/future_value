# 19. future Value

PERCENT = 100

# Helper function
# Takes the present value, interest rate, and time and calculates the future 
# value of the account.
def future_value(pres_val, intrest, time):
    intrest_rate = intrest/PERCENT
    future_amount = pres_val * (1 +  intrest_rate)**time
    return future_amount

# Main funtion accepts all inputs and calculates them with the help of
# future_value(pres_val, intrest, time)
def main():

    pres_val = float(input('Enter the current value of the account:  '))
    intrest = float(input('Enter the monthly interest rate: '))
    time = float(input('Enter the number of months the money will grow in the account: '))
    calculate_future_val = future_value(pres_val, intrest, time)
    print(' ')
    print(f'The value of the account after {time} months will be ${calculate_future_val:,.2f}')
    print(' ')


main()

# Runs the program again if the user enters 'Y'
again = input('Do you want to enter another account? Y/N: ').upper()

while again != 'Y' and again != 'N':
    again = input('Do you want to enter another account? Y/N: ').upper()
while again == 'Y':
    main()
    again = input('Do you want to enter another account? Y/N: ').upper()
