from numpy.random import rand
from numpy.random import randint
import system as sy
import pandas as pd

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

def genetic_algorithm(n_gen, n_pop, n_bits, r_cross, r_mut):
    pop = [randint(0,2,n_bits).tolist() for _ in range(n_pop)]
    
    scores = [0 for i in range(n_pop)]
    best, best_eval = 0, 0

    temp = pd.DataFrame()
    df = pd.DataFrame()

    for gen in range(n_gen):
        callf_arr = sy.write_aelFunction(gen, pop)
        sy.callAelCMD(gen)
        scores = sy.read_fitFunction()
        df = sy.write_df(temp, df, gen, pop, callf_arr,scores)
        for i in range(n_pop):
            if scores[i] > best_eval:
                best, best_eval = pop[i], scores[i]
                print('>Gen %s, new best %s = %s' %(gen, best, best_eval))
        
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
    df.to_csv('df_gens.csv', sep=';')
    return (best, best_eval)
