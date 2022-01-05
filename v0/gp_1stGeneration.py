import numpy as np
from sklearn.utils.random import check_random_state
import pandas as pd

rnd = check_random_state(None)

pop = list([])
pop_size = 20

string1 = "O cromossomo {} é composto pelos genes: {}. A posição das portas é: {}."
f = open("generationsFunction.txt","a+")
g = open("generationsArray.txt","a+")
string2=" ADS_drawCells (28, 28, {}], {}) {}"

for i in range(0,pop_size):
    cro_valid = False
    while (cro_valid == False):

        cro = rnd.randint(0,2,12)#.reshape(4,2)
        pin_point = ""
        #chars = ''.join([str(s) for s in substring])
        for j in range (8, 12):
            pin_point = (pin_point+str(cro[j]))
        pin_point = int(pin_point,2)   

        if (pin_point in [8,10,12,14] and cro[pin_point-7] == 0):
            fit = "fitFunc = 0"  
            cro_valid = False      
        elif (pin_point in [9,11,13,15] and cro[pin_point-9] == 0):
            fit = "fitFunc = 0"
            cro_valid = False
        elif (pin_point < 8 and cro[pin_point] == 0):
            fit = "fitFunc = 0"
            cro_valid = False
        else:
            fit=""
            cro_valid = True

    pop.append(cro)

    crostr = "["+str(cro[0])
    for k in range(1,8):
        crostr = crostr +","+str(cro[k])
    f.write("\n"+str(pop[i]))
    f.write(string2.format(crostr,pin_point, fit))
    g.write("\n"+str(pop[i]))

f.write("\n-----Fim da Geração-----")
f.close()
g.write("\n-----Fim da Geração-----")
g.close()


pop_df = pd.DataFrame(pop)
pop_df.to_csv("Geracao.csv")

print("Esse é um breakpoint para verificar as variáveis.")