#include <stdio.h>

//Prompting inputs
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