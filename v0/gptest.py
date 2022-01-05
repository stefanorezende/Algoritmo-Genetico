import numpy as np
from sklearn.utils.random import check_random_state

rnd = check_random_state(None)

pop = list([])
pop_size = 20
for i in range(0,pop_size):
    x= rnd.randint(0,2,12)#.reshape(4,2)
    pop.append(x)

string1 = "O cromossomo {} é composto pelos genes: {}. A posição das portas é: {}."
f = open("generations.txt","a+")
string2=" ADS_drawCells (28, 28, {}], {}) {}"

for cro, gen in enumerate(pop):
    pin_point = ""
    for j in range (8, 12):
        pin_point = (pin_point+str(gen[j]))
    pin_point = int(pin_point,2)
    print (string1.format(cro,gen,pin_point))

    if (pin_point in [8,10,12,14] and gen[pin_point-7] == 0):
        fit = "fitFunc = 0"
        
    elif (pin_point in [9,11,13,15] and gen[pin_point-9] == 0):
        fit = "fitFunc = 0"
    elif (pin_point < 7 and gen[pin_point] == 0):
        fit = "fitFunc = 0"
    else:
        fit=""
    genstr = "["+str(gen[0])
    for k in range(1,8):
        genstr = genstr +","+str(gen[k])
    f.write("\n"+str(pop[cro]))
    f.write(string2.format(genstr,pin_point, fit))

f.write("\n-----Fim da Geração-----")
f.close()


print("Esse é um breakpoint para verificar as variáveis.")