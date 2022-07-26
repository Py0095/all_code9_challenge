#---------------Libele----------------
# Nan yon tablo nonb, kreye pwòp fason pa w pou w afiche
#  sa ki pi gran, ak sa ki piti a.

number_1 = []
e = 0
# choice_1 = (input('Input a much number you want to put in the list\n>'))
while e <10 :
    number = int(input('Input the number #'+str(e +1)+'\n>'))
    number_1.append(number)
    e +=1
    max_1 = number_1[0]
    min_1 = number_1[0]
for r in number_1:
    if r > max_1:
        max_1 = r
    else:
        min_1 = r
print('The min is: ',min_1)
print('The max is: ',max_1)

