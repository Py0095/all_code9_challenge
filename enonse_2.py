#---------------------Libele---------------------
# Afiche OK si antye N a PA divizib pa 4, afichye NOK nan lòt ka

antre = input('Input whatever integer you want: ')
while not antre.isdigit():
    antre = input('That isn\'t an integer please retry\n> ')
if int(antre) % 4 == 0:
    print('NOK!')
else:
    print('OK!')
        


