#---------------Libele--------------
# Yo ba w antre ak sòti sa yo:

# a = 5                 2
# b = 2         

# a = 3                 3
# b = 4

# a = 1                 1
# b = 1
# Kreye kòd pou input ak output sa yo.
import os 
from time import sleep
clear = lambda:os.system('cls')

print('Input a and b integer.')
sleep(2)
clear()
a = input('input a\n>')
while not a.isdigit():
    a = input(f'*{a}* That isn\'t an integer please retry\n> ')
b = input('input b\n>')
while not b.isdigit():
    b = input(f'*{b}* Please retry that isn\'t an integer\n> ')
a = int(a)
b = int(b)
sleep(2)
clear()

if a > b:
    print(b)
else:
    print(a)

