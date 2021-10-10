#!/usr/bin/python3

def add(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))
    print("Sum of two number is: {}".format(add(num1,num2)))
