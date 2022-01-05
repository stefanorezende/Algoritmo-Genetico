from numpy.random import rand
from numpy.random import randint

def popValid (pop, n_bits):
    pin_arr =[]
    for i in range(0,len(pop)):
        cro_valid = False
        while (cro_valid == False):
            
            pin_point = ''.join([str(pop[i][j]) for j in range(8,12)])
            pin_point = int(pin_point,2)   

            if (pin_point in [8,10,12,14] and pop[i][pin_point-7] == 0):              
                cro_valid = False
                pop[i] = list(randint(0,2,n_bits))    
            elif (pin_point in [9,11,13,15] and pop[i][pin_point-9] == 0):           
                cro_valid = False
                pop[i] = list(randint(0,2,n_bits))
            elif (pin_point < 8 and pop[i][pin_point] == 0):
                cro_valid = False
                pop[i] = list(randint(0,2,n_bits))
            else:
                cro_valid = True
        pin_arr.append(pin_point)
    return(pop, pin_arr)

def write_aelFunction(pop, pin_arr):
    f = open("generationsFunction.txt","a+")
    string1=" ADS_drawCells (28, 28, {}], {})"

    for i in range(0,len(pop)):
        crostr = "["+str(pop[i][0])
        for k in range(1,8):
            crostr = crostr +","+str(pop[i][k])
        f.write("\n"+str(pop[i]))
        f.write(string1.format(crostr,pin_arr[i]))

    f.write("\n-----Fim da Geração-----")
    f.close()

def genetic_algorithm(n_pop, n_cell, n_pin):
    n_bits = int(n_cell/2)+n_pin
    pop = [randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    pop, pin_arr = popValid(pop,n_bits)
    write_aelFunction(pop, pin_arr)
    return (pop, pin_arr)



if __name__ == "__main__":
    n_pop = 20
    n_cell = 16
    n_pin = 4

    pop, pin_arr = genetic_algorithm(n_pop, n_cell, n_pin)
    print(pop)
    print('breakpoint')