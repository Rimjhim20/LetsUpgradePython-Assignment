# Assignment

# Q1. Name the keyword which helps in writing code involving conditions.
# ans- if , elif , else


# Q2. Write the syntax of a simple if statement.
# num = 10
# if None:
#     print("Number is positive")
# print("This will print always")


# Q3. Write a program to check whether a person is eligible for voting or not. (accept age from user)

# age= int(input("Enter age:"))

# if age >=18 :
#     print("Eligible for voting!")
# else:
#     print("Not eligible for voting!")
    
# Q4. What is the output of the given below program?

# if 1 + 3 == 7:
#     print("Hello")
# else:
#     print("Know Program")

#  ans :- Know Program

# Q5. Write a program to check whether a number entered by user is even or odd.

# num = int(input("Enter a number: "))  
# if (num % 2) == 0:  
#    print("{0} is Even number".format(num))  
# else:  
#    print("{0} is Odd number".format(num))  

# Q6. Python program to find the largest element among three Numbers ?

# num1 = 10 
# num2 = 50 
# num3 = 15

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
 
# if (num1 > num2) and (num1 > num3):
#    largest = num1
# elif (num2 > num1) and (num2 > num3):
#    largest = num2
# else:
#    largest = num3
 
# print("The largest number is",largest)


# 07. Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on


x = int(input("Enter a number: "))  

if (x==1):
    print ("Jan")
if (x==2):
    print("Feb")
if (x==3):
    print("March")
if (x==4):
    print("April")
if (x==5):
    print("May")
if (x==6):
    print("June")
if (x==7):
    print("July")
if (x==8):
    print("August")
if(x==9):
    print("September")
if(x==10):
    print("October")
if(x==11):
    print("November")
if(x==12):
    print("December")
if(x<1 or x>12):
    print("Invalid input")

if x == 2:
	print("No. of days: 28/29 days")
elif x in (4,6,9,11):
	print("No. of days: 30 days")
elif x in  (1, 3, 5, 7, 8, 10, 12):
	print("No. of days: 31 day")
else:
	print("Wrong month name") 