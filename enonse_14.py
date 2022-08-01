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
s = (b/a)/2
if s % 2 == 0:
    print(int(s))
else:
    print(s)
