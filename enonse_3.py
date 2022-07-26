#--------------------Libele-----------------------
# Mande itilizate non l. Itilize pwòp teknik pa w pou mete
# non sa nan fòma tit. Sa vle di premye lèt chak mo dwe 
# majiskil, epi lòt yo miniskil. Epi afiche nouvo non an.

# Ekzanp:
# "Ayiti se yon BEL PEYI"  ap vin bay "Ayiti Se Yon Bel Peyi"

text = input('Input your text: ')
while len(text) < 3 or not text.replace(" ", "").isalpha():
    text = input('Invalid text retry please: ')
text_1 = []
text = text.lower()
for i in text.split():
    text_1.append(i[0].upper() + i[1:])
print(" ".join(text_1))
