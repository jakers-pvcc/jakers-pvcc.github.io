# Name: Joshua Akers
# PRICE: 10.99
# SALES TAX: 5.5%

import datetime

## Define Global Variables ##
# Define tax rate and ticket cost
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# Define Variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

## Define Functions ##
def main():
    get_user_data()
    perform_calculations()
    display_results()

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets*PR_TICKET
    sales_tax = subtotal*SALES_TAX_RATE
    total = subtotal+sales_tax

def display_results():
    print('----------------------------')
    print('**** CINEMA MOVIE HOUSE ****')
    print('Your Neighborhood Movie House')
    print('----------------------------')
    print('Tickets     $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax   $ ' + format(sales_tax, '8,.2f'))
    print('Total       $ ' + format(total, '8,.2f'))
    print('----------------------------')
    print(str(datetime.datetime.now()))

## Execute
main()
