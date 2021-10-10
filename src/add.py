#!/usr/bin/python3

def add(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

if __name__ == "__main__":
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))
    num3 = int(input("Enter num3:"))
    sum_list = [num1, num2, num3]
    sum = add(num_list)
    print("Number list: {} and Sum of list is {}".format(num_list, sum))
