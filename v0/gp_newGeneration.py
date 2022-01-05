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

df["Rank"] = x
df_sorted = df.sort_values("Rank",ascending =False)


reproduce = np.array(df_sorted.iloc[1,1:13])

rnd1 = check_random_state(1)
rnd2 = check_random_state(2)

cross_pool = list ([])
pool_size = 7
for i in range(1,pool_size+1):
    cross_pool.append(np.array(df_sorted.iloc[i,1:13]))

print("O poll é: ", cross_pool)    
new_gen = list([])
for i, cro in enumerate (cross_pool):
# ale = rnd1.randint(0,pool_size-1)
    cro_cross = cross_pool[i]
#ale2 = rnd2.randint(0,pool_size-1)    
    if(i<len(cross_pool)-1):
        donner = cross_pool[i+1]
    else:
        donner = cross_pool[0]    
    gens = rnd.randint(0,len(cro_cross)-1,3)

    for j in gens:
        new_cro = cro_cross
        new_cro [j] = donner [j]

    new_gen.append(new_cro)
string1 = "O Cromos escolhido é {}. O Donner é: {}. E o Novo cromos é {}. GEN {}"
print(string1.format(cro_cross, donner, new_cro, gens))

print("breakpoint")


# print (df_sorted)
# print (reproduce)
# print (cross_pool)

# g = open("C:\\Users\\stefa\\Desktop\\Python\\generationsArray.txt", "r")

# gl = g.readlines() # readlines reads the individual lines into a list
# y= pd.DataFrame([])
# for i in gl:
#      y.append(i) 
# print(y)

pop = new_gen


string1 = "O cromossomo {} é composto pelos genes: {}. A posição das portas é: {}."
f = open("generationsFunction2.txt","a+")
g = open("generationsArray2.txt","a+")
string2=" ADS_drawCells (28, 28, {}], {}) {}"

for i in range(0,len(pop)):
    cro_valid = False
    while (cro_valid == False):

        pin_point = ""
        for j in range (8, 12):
            pin_point = (pin_point+str(cro[j]))
        pin_point = int(pin_point,2)   

        if (pin_point in [8,10,12,14] and cro[pin_point-7] == 0):
            fit = "fitFunc = 0" 
            cro = rnd.randint(0,2,12)#.reshape(4,2) 
            cro_valid = False      
        elif (pin_point in [9,11,13,15] and cro[pin_point-9] == 0):
            fit = "fitFunc = 0"
            cro = rnd.randint(0,2,12)#.reshape(4,2)
            cro_valid = False
        elif (pin_point < 8 and cro[pin_point] == 0):
            fit = "fitFunc = 0"
            cro = rnd.randint(0,2,12)#.reshape(4,2)
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