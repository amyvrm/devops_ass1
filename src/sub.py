#!/usr/bin/python3

def sub(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))

    sum = sub(num1, num2)
    print("Subtraction of {} and {} numbers is {}".format(num1, num2, sum))
