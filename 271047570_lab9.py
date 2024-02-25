############################################# Lab 9 #####################################################

#Task1
print("Task 1")
def add(list):
    result= 0
    for num in list:
        result=result+num
    return result
def sub(list):
    result= list[0]
    for num in list[1:]:
        result=result-num
    return result
def mul(list):
    result= lst[0]
    for num in list:
        result=result*num
    return result 
def div(list):
    result= list[0]
    for num in list[1:]:
        if num!=0:
            result=result/num
        else:
            return "Not divisible"    
    return result
           
# #Example
lst=[1,2,-3,4]
print(f"Addition:", add(lst))
print(f"Subtraction:", sub(lst))
print(f"Multiplication:", mul(lst))
print(f"Division:", div(lst))

#Task2
print("Task 2")

def separate_indexes(lst):
    even_indexed = []
    odd_indexed = []
    for num in range(len(lst)):
        if num % 2 != 0:
            odd_indexed.append(lst[num])
        else:
            even_indexed.append(lst[num])
    return even_indexed, odd_indexed

#Example
lst= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1,list2 = separate_indexes(lst)
print("Odd index list:", list1)
print("Even index list:", list2)


#Task3
print("Task 3")

def separator(lst):
    even_sum = 0
    odd_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_sum=even_sum+num
        else:
            odd_sum=odd_sum+num
    return even_sum, odd_sum

#Example
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_sum, odd_sum = separator(list)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#Task4
print("Task 4")

def Reverse(lst):
    reversed_list = []

    for num in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[num])
    return reversed_list

#Example
random_numbers = [1,2,3,4,5]
reversed_numbers = Reverse(random_numbers)
print("Original list:", random_numbers)
print("Reversed list:", reversed_numbers)

# Task5
print("Task 5")

def first_last(lst1, lst2):
    combined_names = []

    for first, last in zip(lst1, reversed(lst2)):
        combined_names.append([first, last])
    return combined_names

#Example
first_names = ["Ali", "Ahad", "Wasi", "Waqas", "Shaaz"]
last_names = ["Qumail", "Wali", "Shah", "Asif", "Bari"]
result = first_last(first_names, last_names)
print("Output:")
for item in result:
    print(item)



    

