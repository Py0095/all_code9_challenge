import os
from time import sleep
clear = lambda:os.system('cls')
print('Input an interval!')
a = (input('first:'))
while not a.isdigit():
    a = (input(f'"{a}" That isn\' an integer retry please:\na:>'))
a1 =(input('second:'))
while not a1.isdigit():
    a1 = (input(f'"{a1}" That isn\' an integer retry please:\na1:>'))
while int(a) > int(a1) :
    print(f'Please retry "a1= {a1}" should a1e greather than "a= {a}".')
    a = (input('first:'))
    a1 = (input('second:'))
a = int(a)
a1 = int(a1)
#print('Input 2 integer.')
sleep(2)
clear()
x = input('input x\n>')
while not x.isdigit():
    x = input('That isn\'t an integer please retry\n> ')
x1 = input('input y\n>')
while not x1.isdigit() or int(x1) % 2 == int(x) % 2:
    x1 = input('Please retry\n> ')
sleep(2)
clear()

x = int(x)
x1 = int(x1)

print("------------------------------------------")
print("                                          ")
print(f"multiple {x} / NOT multiple {x1}")
e = ''
sum = 0
for i in range(a,a1):
    if (i%x)==0 and (i%x1)!=0:
        sum = sum + 1
        e +=str(i)+','
print("number:",e.strip(','),f"->total :{sum}")
print("------------------------------------------")
print("                                          ")
print(f"multiple {x1} / NOT multiple {x}")
e1 = ''
sum1 = 0
for i in range(a,a1):
    if (i%x)!=0 and (i%x1)==0:
        sum1 = sum1 + 1
        e1 +=str(i)+','
print("number:",e1.strip(','),f"->total :{sum1}")

print("------------------------------------------"
      "                                          "
      "                                          ")
print(f"multiple {x} / NOT multiple {x1}")  
e2 = ''
sum2 = 0
for i in range(a,a1):
    if (i%x)==0 and (i%x1)==0:
        sum2 = sum2 + 1
        e2 +=str(i)+','
print("number:",e2.strip(','),f"->total {sum2}")

print("------------------------------------------"
      "                                          "
      "                                          ")
print(f" NOT multiple {x} / NOT multiple {x1} ")
e3 = ''
sum3 = 0
for i in range(a,a1):
    if (i%x)!=0 and (i%x1)!=0:
        sum3 = sum3 + 1
        e3 +=str(i)+','
print("number:",e3.strip(','),f"->total {sum3}")

