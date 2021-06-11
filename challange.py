print("Would you like to continue? ")
cont = input()
if cont == 'n' or cont == "no":
    print("Exiting")
elif cont == 'y' or cont == 'yes':
    print('Continuing ...')
    print('Complete!')
else:
    print("Please try again and respond with yes or no.")
