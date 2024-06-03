
def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print(numbers)

#Checking odd or even numbers in a range.
def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print (f"{number} is even")
        else:
            print(f"{number} is odd")           


#Checking Divisibility
def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
            print (f"{number} is divisible by 2")
        elif number%3 == 0:
            print (f"{number} is divisible by 3")
        elif number%5 == 0:
            print (f"{number} is divisible by 5")
        elif number%7 == 0:
            print (f"{number} is divisible by 7")
        else:
            print (f"{number} is not divisible by 2,3,5 and 7")
        
#Creating a countdown
def countdown(n):
    while n > 0 :
        print (n)
        n-= 1

def countdown_to_five(n):
    while n > 0:           

        print(n)
        if n ==5:
           break
        n -= 1
#checking divisibility using continue(skips and goes to the next number).
def divisible_by_seven(n):
    x = 1
    while x <= n:
        x += 1
        if x%7!= 0:
            continue
        print(x)

# Using if, else, elif create a function called fizzbuzz that accepets a number n and
# generates a range of numbers from 0 to n.
# 1. for numbers divisible by 3 print fizz
# 2. for numbers divisible by 5 print Buzz
# 3. for other numbers print fizzbuzz
# Invoke the numbers as fizzbuzz(10) and fizzbuzz(100)

def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number%3 == 0:
            print(f"fizz")
        elif number%5 == 0:
            print(f"buzz")
        else:
            print (f"fizzbuzz")

# Using while, if and continue create a function to print all the even numbers from 0 to 50.

def even_numbers(n):
    number = 0
    while number<=n:
        number += 1
        if number % 2!= 0:
            continue
        print(number)



# followers ={}
# def add_user(follower):
#     if follower in followers:
#         if follower in followers[user]:
#             print("Already Exists")
#         else:
#             followers[user].append(follower)
#     else:
#         follower[user] = [follower]            



 
    
        

