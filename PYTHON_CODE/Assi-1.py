#Ques-1  Write a python program to find the GCD of two number (take input from the user) using Euclid's algorithm.

# def gcd(a, b):
#     while b != 0:
#          a, b = b, a % b
#     return a

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("The GCD of", num1, "and", num2, "is:", gcd(num1, num2))    




















# # Ques-2 Write a python program to find the factorial of any given positive integer
# #        (take input from the user).

# def factorial(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
#         return n * factorial(n - 1)

# num = int(input("Enter a positive integer: "))

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print("The factorial of", num, "is:", factorial(num))





# # # Ques-3 Write a program that print the sum of the digits of a positive integer n. 
# # #         Program to find sum of digits of a positive integer

# # def sum_digit(x):
# #     sum=0
# #     for i in x:
# #         num=int(i)
# #         sum+=num
# #     return sum 
    
# # number=(input("Enter no.:"))
# # print(sum_digit(number))

  






















# # # Ques-4 Write a python program that prints whether a given year is a leap year or not.
# # #        Take input from the user.

# # # year = int(input("Enter a year: "))

# # # if (year % 4 == 0):
# # #     print(year, "is a leap year")
# # # else:
# # #     print(year, "is not a leap year")
























# # # Ques-5 Write a python program that takes as input the time of the day, and greets
# # #        good morning ,good afternoon,or good evening depending on the time. You
# # #        can assume a suitable time, such as the afternoonor evening.  Program to greet based on the time of the day

# # # time = int(input("Enter the hour of the day (0-23): "))

# # # if time < 0 or time > 23:
# # #     print("Invalid time. Please enter between 0 and 23.")
# # # elif 5 <= time < 12:
# # #     print("Good Morning!")
# # # elif 12 <= time < 17:
# # #    print("Good Afternoon!")
# # # elif 17 <= time < 21:

# # #      print("Good Evening!")
# # # else:
# # #     print("Good Night!")  






















#  Ques-6 Write a python program to play Rock,Paper,Scissors with the computer.(rock defeats scissor,scissor defeat                                       
#        paper,paper defeat rock,same-same is a tie).Keep count of your scores,including ties and print at the end.
#         You need to use the concept of:
#        Variable
#        while
#         for
#         random
#         breakimport random

# import random
# player=input("choose Rock,paper or scissors:")
# pl = player.lower()
# computer = random.choice(["rock","Paper","scissors"])

# if pl == computer:
#     print("TIE!!")
# elif (pl == "rock" and computer =="scissor"):
#     print("WIN!!")
# elif (pl == "scissor" and computer =="paper"):
#     print("WIN!!")
# elif (pl == "paper" and computer =="rock"):
#     print("WIN!!")
# else:
#     print("LOST!!")