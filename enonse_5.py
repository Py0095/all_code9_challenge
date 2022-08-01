#---------------------Libele------------------
# Yo ba w yon chenn karaktè ki gen plizyè nonb ladan ki separe ak espas. Kalkile pwodwi, total chak dijit ki konpoze chak nonb.

# Ekzanp:

# "5 45 123 12"
# ap bay (5) * (4+5) * (1+2+3) * (1+2) => 5*9*6*3
# ki bay total: 810
input_1 = input('Input\n>>>')

p = 1
print(input_1)
prod = 1
for i in input_1.split(' '):
    s = 0
    for e in range(len(i)):
         s += int(i[e])
    p *=s
print(p)   
        

    

      
 