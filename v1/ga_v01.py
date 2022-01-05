from numpy.random import rand
from numpy.random import randint

n_pop = 20
n_cell = 16
n_pin = 4
n_bits = int(n_cell/2)+n_pin


# pop = [randint(0,2,n_bits).tolist() for _ in range(n_pop)]
pop = list([])

f = open("generationsFunction.txt","a+")
string1=" ADS_drawCells (28, 28, {}], {})"

for i in range(0,n_pop):
    cro_valid = False
    while (cro_valid == False):

        cro = randint(0,2,n_bits)

        pin_point = ''.join([str(cro[j]) for j in range(8,12)])
        pin_point = int(pin_point,2)   

        if (pin_point in [8,10,12,14] and cro[pin_point-7] == 0):              
            cro_valid = False      
        elif (pin_point in [9,11,13,15] and cro[pin_point-9] == 0):           
            cro_valid = False
        elif (pin_point < 8 and cro[pin_point] == 0):
            cro_valid = False
        else:
            cro_valid = True

    pop.append(cro)

    crostr = "["+str(cro[0])
    for k in range(1,8):
        crostr = crostr +","+str(cro[k])
    f.write("\n"+str(pop[i]))
    f.write(string1.format(crostr,pin_point))

f.write("\n-----Fim da Geração-----")
f.close()


print('breakpoint')