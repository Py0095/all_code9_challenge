#----------------Libele------------------
# Ou gen yon chenn karaktè, ranvèse tout karaktè yo san pa gen okenn espas,
# Ekzanp:
# "Ayibobo Ayiti" => "itiyAobobiyA"

text = input('Input your text: ')
text_1 =''
while not text.replace(" ", "").isalpha():
    text = input('Invalid text retry please: ')
text = text.replace(' ','')
text_1 = ''.join(reversed(min(text.split(),key=len))) 
# text_1 = text[::-1] That is another maner to inverse
print(text_1.capitalize().replace(' ',''))
