#include <stdio.h>

# intro prompt
print("Welcome to the 'Ancient Egyptian' multiplication algorithm!")
print("Here we will use an ancient method to find the product of two numbers!")
print("===========================================================================")

# Prompting inputs
while True:
    numOne = int(input("Begin by entering the first positive number you want to multiply: "))

    while numOne < 0:
        print(f"\nError: Please enter a valid positive number!")
        numOne = int(input("\nBegin by entering the first positive number you want to multiply: "))

    numTwo = int(input("\nNext, enter the second positive number: "))

    while numTwo < 0:
        print(f"\nError: Please enter a valid positive number!")
        numTwo = int(input("\nNext, enter the second positive number: "))

    # If Product of zero
    if numOne == 0 or numTwo == 0:
        print("\nAnything multiplied by 0 will be 0. Please try again with different numbers!")

    #Bools for determining negative values (False = negative and True = Positive)
    #if numTwo < 0 and numOne > 0:
        #var1 = False
    #print(bool(var1))
    #elif numTwo < 0 and numOne < 0:
        #var2 = True
        #rint(bool(var2)) 

    # Calculations (THAT IS SO EXTRA FOR NO REASON)
    while numTwo != 0:
        if numTwo % 2 == 0:
            print(f"   |     Since {numTwo} is even, we will ignore {numOne} \n")
        elif (numTwo %2 != 0):
            print(f"   |     Since {numTwo} is odd, we will add {numOne} to the final product \n")
            product = 0
            product = product + numOne
        numTwo = numTwo / 2
        numOne = numOne * 2

        # Printing the results! (Keep them fingers CROSSED)
        print("\n")
        print(f"The product is: {product} \n")

        # Prompt asking if the user wants to do another calculation (and also to stop the infinite loop lol)
        symbol = str(input("Would you like to compute more? (Y/N): "))
        if symbol == 'Y':
            continue

        print("Thank you for using the 'Ancient Egyptian' multiplication algorithm! Goodbye!")
        break




