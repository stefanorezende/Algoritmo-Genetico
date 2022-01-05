from numpy.random import rand
from numpy.random import randint
import os
import time

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

def write_aelFunction(n_gen, pop, pin_arr):
    filename = 'gen{}\\ind{}.ael'
    string1 = "\nADS_drawCells (28, 28, {}], {});\n"    

    for i in range(0,len(pop)):
        f = open (filename.format(n_gen,i),"a+")
        crostr = "["+str(pop[i][0])
        for k in range(1,8):
            crostr = crostr +","+str(pop[i][k])
        # f.write("\n"+str(pop[i]))
        f.write(string1.format(crostr,pin_arr[i]))
        # f.write("\n-----Fim da Geração-----")
        f.close()

def callAelCMD ():
    arqv = os.listdir('gen1')
    comm = 'ads -m gen1\\{}'
    for fileael in arqv:
        os.system(comm.format(fileael))
        # os.system(r'ads -m C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\AEL\\ADS_layout_drawCells_v2.ael')
        time.sleep(60)
        os.system(r'taskkill/im hpeesofde.exe')

def read_fitFunction():
    f = open('C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\python\\fitFunction.txt',"r")
    fl = f.read().splitlines() 
    scores = [float(item) for item in fl]
    return (scores)
        
def selection(pop, scores, k=3):
	# first random selection
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		# check if better (e.g. perform a tournament)
		if scores[ix] < scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]        

# crossover two parents to create two children
def crossover(p1, p2, r_cross):
	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()
	# check for recombination
	if rand() < r_cross:
		# select crossover point that is not on the end of the string
		pt = randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]

# mutation operator
def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		# check for a mutation
		if rand() < r_mut:
			# flip the bit
			bitstring[i] = 1 - bitstring[i]

def genetic_algorithm(n_pop, n_cell, n_pin):
    n_gen = 1
    n_bits = int(n_cell/2)+n_pin
    pop = [randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    pop, pin_arr = popValid(pop,n_bits)
    write_aelFunction(n_gen, pop, pin_arr)
    callAelCMD()
    return (pop, pin_arr)



if __name__ == "__main__":
    n_iter = 3
    n_pop = 20
    n_cell = 16
    n_pin = 4
    r_cross = 0.9
    r_mut = 1.0/float(n_cell)

    # pop, pin_arr = genetic_algorithm(n_pop, n_cell, n_pin)

    pop = [[0,0,0,1,0,1,0,1], [0,1,0,0,1,1,0,0],[1,0,1,1,0,0,1,1],[0,0,1,1,1,0,0,0],[0,1,0,0,0,0,1,0],
    [1,0,0,1,0,1,1,0],[1,0,1,0,1,1,0,0],[1,0,1,0,1,1,1,0],[1,0,0,1,1,1,1,1],[1,1,0,0,0,1,0,0],
    [1,1,0,1,1,1,0,0],[1,1,1,0,1,1,1,0],[0,0,1,0,1,1,1,0],[1,0,0,1,1,1,0,0],[0,1,0,0,0,1,1,0],
    [1,1,1,1,0,1,1,0],[0,0,0,1,0,1,0,0],[1,1,1,1,1,0,0,0],[1,0,0,0,0,1,0,1],[1,1,1,0,1,0,1,0]]

    pin_arr = [10, 1, 0, 11, 1, 15, 13, 11, 15, 12, 5, 15, 13, 5, 8, 5, 3, 9, 12, 9]

    scores = read_fitFunction()

    best, best_eval = 0, 0
    for gen in range(n_iter):
        for i in range(n_pop):
            if scores[i] > best_eval:
                best, best_eval = pop[i], scores[i]
                print(">Gen{}, new best {} {}= {}".format(gen, pop[i],  pin_arr[i], scores[i]))
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]

        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i+1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
        print('Nova População',pop)

    print('breakpoint')