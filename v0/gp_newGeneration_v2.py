import numpy as np
import pandas as pd
from sklearn.utils.random import check_random_state
# import random as rnd


rnd = check_random_state(None)
f = open("C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\python\\fitFunction.txt", "r")

fl = f.readlines() # readlines reads the individual lines into a list
x=[]
for i in fl:
     x.append(float(i))
print (x)

df = pd.read_csv("Geracao.csv")

df = df.astype(int)

df["Rank"] = x
df_sorted = df.sort_values("Rank",ascending =False)

# df_sorted = df_sorted.to_numpy().astype(int)

reproduce = df_sorted.head(1)
reproduce = reproduce.to_numpy().astype(int)

rnd1 = check_random_state(1)
rnd2 = check_random_state(2)

cross_pool = df_sorted.head(7)
cross_pool = cross_pool.to_numpy().astype(int)

print("O poll é: ", cross_pool)    

new_gen = list([])
# cro_cross = np.array([])
# donner = np.array([])
# new_cro = np.array([])
for i in range(0, len(cross_pool)):
    cro_cross  = cross_pool[i]

    for j in range(0, len(cross_pool)):
        if(i == len(cross_pool)-1):
            donner = cross_pool[0]    
            gens = rnd.randint(1,len(cro_cross)-1,3)

            for k in gens:
                new_cro = cro_cross
                new_cro [k] = donner [k]
        else:
            donner = cross_pool[i+1]    
            gens = rnd.randint(1,len(cro_cross)-1,3)

            for k in gens:
                new_cro = cro_cross
                new_cro [k] = donner [k]

        new_gen.append(new_cro)
string1 = "O Cromos escolhido é {}. O Donner é: {}. E o Novo cromos é {}. GEN {}"
print(string1.format(cro_cross, donner, new_cro, gens))

print("breakpoint")

pop = new_gen

newpop = list([])
string1 = "O cromossomo {} é composto pelos genes: {}. A posição das portas é: {}."
f = open("generationsFunction2.txt","a+")
g = open("generationsArray2.txt","a+")
string2=" ADS_drawCells (28, 28, {}], {})"

# for i in range(0,len(pop)):
#     cro_valid = False
    # while (cro_valid == False):
for i in pop:
    cro = i
    pin_point = ""
    for j in range (9, 13):
        pin_point = (pin_point+str(cro[j]))
    pin_point = int(pin_point,2)   

            # if (pin_point in [8,10,12,14] and cro[pin_point-7] == 0):
            #     fit = "fitFunc = 0" 
            #     cro = rnd.randint(0,2,12)#.reshape(4,2) 
            #     cro_valid = False      
            # elif (pin_point in [9,11,13,15] and cro[pin_point-9] == 0):
            #     fit = "fitFunc = 0"
            #     cro = rnd.randint(0,2,12)#.reshape(4,2)
            #     cro_valid = False
            # elif (pin_point < 8 and cro[pin_point] == 0):
            #     fit = "fitFunc = 0"
            #     cro = rnd.randint(0,2,12)#.reshape(4,2)
            #     cro_valid = False
            # else:
            #     fit=""
            #     cro_valid = True

    newpop.append(cro)

    crostr = "["+str(cro[1])
    for k in range(2,9):
        crostr = crostr +","+str(cro[k])
    f.write("\n"+str(i))
    f.write(string2.format(crostr,pin_point))
    g.write("\n"+str(i))

f.write("\n-----Fim da Geração-----")
f.close()
g.write("\n-----Fim da Geração-----")
g.close()


print("Esse é um breakpoint para verificar as variáveis.")