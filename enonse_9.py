print('Input an interval!')
a = (input('first:'))
while not a.isdigit():
    a = (input(f'"{a}" That isn\' an integer retry please:\na:>'))
b =(input('second:'))
while not b.isdigit():
    b = (input(f'"{b}" That isn\' an integer retry please:\nb:>'))
while int(a) > int(b) :
    print(f'Please retry "b= {b}" should be greather than "a= {a}".')
    a = (input('first:'))
    b = (input('second:'))
number = range(int(a),int(b))
tab = []
for i in number:
    if int(i) % 2 == 0:
        tab.append(i)
t = sum(tab)
print('The sum is:',t)
