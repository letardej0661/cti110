# This program calculates and displays travel expenses
# 2/16/2023
# CTI-110 P1HW2 - Travel Expense
# Jennifer Letarde

print ('Enter budget:', end=' ')
budget = int(input())

print ('Enter travel destination:', end=' ')
destination = input()

print ('How much do you think you will spend on gas?', end=' ')
gas_cost = int(input())

print ('Approximately, how much will you need for accomadation/hotel?', end=' ')
hotel_cost = int(input())

print ('Last, how much do you need for food?', end=' ')
food_cost = int(input())

print ('------Travel Expenses------')
print ('Location:', destination)
print ('Initial Budget:', budget)
print ()
print ('Fuel:', gas_cost)
print ('Accomodation:', hotel_cost)
print ('Food:', food_cost)
print ()
print ('Remaining Balance:', budget - (gas_cost + hotel_cost + food_cost))
