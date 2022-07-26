#---------------Libele----------------
# Ou dwe rantre nan yon pòt(PORT) ki ouvri. Ou pa gen anpil 
# tan pou skane tout pòt yo, men ou konnen pòt ki ouvri a, li 
# egal total tout dijit yo ki nan adrès IP a, miltiplye pa 
# premye dijit ki nan adrès IP a.Mande itilizatè a pou l tape
#  adrès IP a, epi afiche pòt ki ouvri a

# NB: Tout adrès ip separe ak pwen(.)

# Ekzanp:
# "127.0.0.1" ap bay rezilta
# (1+2+7+0+0+1) * 1 = 11 =>
# Donk pòt ki ouvri a se 11

addresse_1 = input('Input your ip address: ')
output = 0
for i in addresse_1.split('.'):
    for el in i:
        output += int(el)
output = output * int(addresse_1[0])
print(output)