    #-----------------------Libele--------------------
    # Yo ba w yon textenn karaktè, ranplase tout karaktè ki plase devan yon vwayèl pa asteriks(*). Epi afitexte nouvo textenn karaktè a.a

text = input('Input your text: ')
while len(text) < 3 or not text.replace(" ", "").isalpha():
    text = input('Invalid text retry please: ')
text = text.strip().title()
voyelle = "aeiouy"
for i in range(len(text)) :
    if text[i] in voyelle:
        text = text.replace(text[i-1],"*")
print(text)

