#!/usr/bin/env python3

def main():
    #get input from user
    first = float(input("Enter a number: "))
    second = float(input("Enter a another number: "))
    operator = input("Enter a math operator (+,-,*, or /): ")
    answer = float(input("Enter the answer: "))
    result = 0
    #figure out which operator was input
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    else:
        print("Incorrect. Try again!")
    return
    #Determine if the user did the math correctly
    if answer == result:
        print("Correct! Good job.")
    else:
      print("Incorrect. Try again!")
if __name__ == "__main__": main()