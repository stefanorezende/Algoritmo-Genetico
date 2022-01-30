from numpy.random import rand
from numpy.random import randint
import os
import time
import shutil

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

def write_aelFunction(gen, pop, pin_arr):
    dirName = 'gen{}'
    filename = 'ind{}.ael'
    filename0 = 'ind0{}.ael'
    string1 = '\ndecl context = de_get_design_context_from_name("AEL_Python_lib:gen{}:layout");'
    string2 = '\nde_show_context_in_new_window(context);'
    string3 = "\nADS_drawCells (28, 28, {}], {});\n"    

    # Create target Directory if don't exist
    if not os.path.exists(dirName.format(gen)):
        os.mkdir(dirName.format(gen))
        print("Directory " , dirName.format(gen) ,  " Created ")
    else:    
        print("Directory " , dirName.format(gen) ,  " already exists")

    for i in range(0,len(pop)):
        if i < 10:
            shutil.copyfile('model.ael', '{}\\{}'.format(dirName.format(gen),filename0.format(i)))
            f = open ('{}\\{}'.format(dirName.format(gen),filename0.format(i)),"a+")
        else:
            shutil.copyfile('model.ael', '{}\\{}'.format(dirName.format(gen),filename.format(i)))
            f = open ('{}\\{}'.format(dirName.format(gen),filename.format(i)),"a+")
        crostr = "["+str(pop[i][0])
        for k in range(1,8):
            crostr = crostr +","+str(pop[i][k])
        f.write(string1.format(gen))
        f.write(string2)
        f.write(string3.format(crostr,pin_arr[i]))
        # f.write("\n-----Fim da Geração-----")
        f.close()

    # decl context;
    # context = de_get_design_context_from_name("AEL_Python_lib:gen0:layout");
    # de_show_context_in_new_window(context);
    # ADS_drawCells (28, 28, [0,0,1,1,0,0,1,1], 2);

def callAelCMD (gen):
    arqv = os.listdir('gen{}'.format(gen))
    comm = 'ads -m gen{}\\{}'
    for fileael in arqv:
        os.system(comm.format(gen,fileael))
        print(comm.format(gen,fileael))
        os.system(r'ads -m C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\AEL\\ADS_layout_drawCells_v2.ael')
        time.sleep(45)
        os.system(r'taskkill/im hpeesofde.exe /f')

def read_fitFunction(gen):
    filename = 'C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\python\\fitFunction{}.txt'
    f = open(filename.format(gen),'r')
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

def genetic_algorithm(n_gen, n_pop, n_cell, n_pin, r_cross, r_mut):
    n_bits = int(n_cell/2)+n_pin
    pop = [randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    
    scores = [0 for i in range(n_pop)]
    best, best_eval = 0, 0

    for gen in range(n_gen):
        pop, pin_arr = popValid(pop,n_bits)
        write_aelFunction(gen, pop, pin_arr)
        callAelCMD(gen)
        scores = read_fitFunction(gen) 
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

    return (best, best_eval)



if __name__ == "__main__":
    n_gen = 8
    n_pop = 20
    n_cell = 16
    n_pin = 4
    r_cross = 0.9
    r_mut = 1.0/float(n_cell)

    best, best_eval = genetic_algorithm(n_gen, n_pop, n_cell, n_pin, r_cross, r_mut)

    bestString = '\nBest = {} Fit = {}'
    print('Done!')
    print (bestString.format(best,best_eval))
    bfile = open("BestEvaluation.txt","a+")
    bfile.write(bestString.format(best,best_eval))
    bfile.close()
    # pop = [[0,0,0,1,0,1,0,1], [0,1,0,0,1,1,0,0],[1,0,1,1,0,0,1,1],[0,0,1,1,1,0,0,0],[0,1,0,0,0,0,1,0],
    # [1,0,0,1,0,1,1,0],[1,0,1,0,1,1,0,0],[1,0,1,0,1,1,1,0],[1,0,0,1,1,1,1,1],[1,1,0,0,0,1,0,0],
    # [1,1,0,1,1,1,0,0],[1,1,1,0,1,1,1,0],[0,0,1,0,1,1,1,0],[1,0,0,1,1,1,0,0],[0,1,0,0,0,1,1,0],
    # [1,1,1,1,0,1,1,0],[0,0,0,1,0,1,0,0],[1,1,1,1,1,0,0,0],[1,0,0,0,0,1,0,1],[1,1,1,0,1,0,1,0]]

    # pin_arr = [10, 1, 0, 11, 1, 15, 13, 11, 15, 12, 5, 15, 13, 5, 8, 5, 3, 9, 12, 9]

    print('breakpoint')