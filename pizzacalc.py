# Joshua C. Akers
# PP: Calculate Pizza orders
# Error Notes: This version is heavily flawed. Cannot figure out how to separate each type, and they all run at once. The display() only gives
# the last total available.

import datetime

# Define Price
small_p = 9.99
medium_p = 12.99
large_p = 14.99
elarge_p = 17.99

# Tax Rate
sales_tax = .055

#Define var
num_p = 0
subtotal = 0
stax = 0
total = 0

#Define Type
type_s = 1
type_m = 1
type_l = 1
type_el = 1

## Define Funct
def main():
    coll_data()
    calc()
    display()
    main()

def coll_data():
    global num_p
    num_p = int(input("Number of Pizzas: "))
    print('You will be asked which size you want. Do not enter more than 1 size at a time.')
    type_s = int(input("Enter 1 for Small: Enter 0 to say no: "))
    type_m = int(input("Enter 1 for Medium: Enter 0 to say no: "))
    type_l = int(input("Enter 1 for Large: Enter 0 to say no: "))
    type_el = int(input("Enter 1 for Extra Large: Enter 0 to say no: "))
    

def calc():
    global type_s, type_m, type_l, type_el, total, subtotal, sales_tax, small_p, medium_p, large_p, elarge_p
    if type_s == 1:
        subtotal = num_p*small_p
        stax = subtotal*sales_tax
        total = subtotal + stax

    if type_m == 1:
        subtotal = num_p*medium_p
        stax = subtotal*sales_tax
        total = subtotal + stax

    if type_l == 1:
        subtotal = num_p*large_p
        stax = subtotal*sales_tax
        total = subtotal + stax
    
    if type_el == 1:
        subtotal = num_p*elarge_p
        stax = subtotal*sales_tax
        total = subtotal + stax
        
def display():
    if type_s == 1:
        print('----------------------------------')
        print('Total (Small)        $ ' + format(total, '10,.2f'))
        print('----------------------------------')
         
    if type_m == 1:
        print('----------------------------------')
        print('Total (Medium)        $ ' + format(total, '10,.2f'))
        print('----------------------------------')
        
    if type_l == 1:
        print('----------------------------------')
        print('Total (Large)        $ ' + format(total, '10,.2f'))
        print('----------------------------------')
        
    if type_el == 1:
        print('----------------------------------')
        print('Total (E. Large)        $ ' + format(total, '10,.2f'))
        print('----------------------------------')
        
    











#Execution
main()
    
