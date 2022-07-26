#----------------Libele-----------------------
# Ou gen yon sekans karaktè ki separe ak espas. Men kòman eskrip la prezante:

# Yon karaktè reprezante direksyon mouvman wap fè a 
# (> demare pou ale adwat | < demare pou ale agoch)
# Yon kantite deplasman ou dwe fè
# Yon karaktè ki sèvi referans apati kibò w dwe deplase.
# Ekzanp:

# ">2T" : 2 deplasman adwat apati karaktè "T" a, ki vin bay "V"
# "<5S" : 5 deplasman agoch soti nan karaktè "S" la, ki vin bay "N"

# Men kèk done (INPUT) ak repons yo (OUTPUT):

#     ">5K <0Y <3W <3K <6U <3Q" ap bay "PYTHON"
#     "14P <1V <1H >4O" ap bay "TUGS"

import string
a = string.ascii_uppercase
def dekode(entre):
    # entre = '<5X >2G >2R >0E <5R <0A >5K'
    entre = entre.split()
    mot = ''
    for i in entre:
        for t in i:
            if i[0]=='<': 
                idx = a.index(i[2]) -int(i[1])
            else:
                idx = a.index(i[2]) + int(i[1])
        mot +=a[idx]
    return mot

d = input('Input the sentence you want to decryted: ')
print(dekode(d))