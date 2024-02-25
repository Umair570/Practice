############################################## Lab 7 ###############################################

#Task1
def power(base,exponent):
    result=1
    while exponent  >0:
        result=result*base
        exponent=exponent-1
    return result   

base=float(input("enter the base:"))
exponent=int(input("enter the exponent:"))
result=power(base,exponent)
print(base,"^",exponent,"is equal to",result)

#Task2
def palindrome(arg):
    count=0
    while count<=5:
        result=arg[:len(input_1)] == arg[::-1]
        return result
    count=count+1

input_1=input("enter the input to check:")
print(palindrome(input_1))

#Task3
def factors(arg):
    x=1
    while x<=arg:
        if arg%x==0:
            print(x)
        x=x+1
input_2=int(input("enter the number:"))
factors(input_2)

#Task4
def sum_of_digits(arg1,arg2,arg3,arg4,arg5):
    s=str(arg1)+str(arg2)+str(arg3)+str(arg4)+str(arg5)
    sum=0
    count=0
    while (count!=len(s)):
        sum=sum+int(s[count])
        count=count+1
    return sum

s=sum_of_digits(2,3,4,5,6)
print(s)

#Task 5
def binary_to_decimal(binary_number):
    decimal_number = 0
    position = 0

    binary_number = binary_number[::-1]  

    while position < len(binary_number):
        if binary_number[position] == "1":
            decimal_number += 2**position
        position += 1

    return decimal_number

binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(binary_number)
print("The decimal equivalent is:",decimal_number)




