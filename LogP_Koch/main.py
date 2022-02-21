from numpy.random import rand
from numpy.random import randint
from ga import genetic_algorithm

if __name__ == "__main__":
    n_gen = 10
    n_pop = 6   # Must be a integer pair
    n_bits = 85
    r_cross = 0.9
    r_mut = 1.0/float(n_bits)

    best, best_eval = genetic_algorithm(n_gen, n_pop, n_bits, r_cross, r_mut)

    bestString = '\nBest = {} Fit = {}'
    print('Done!')
    print (bestString.format(best,best_eval))
    bfile = open("BestEvaluation.txt","a+")
    bfile.write(bestString.format(best,best_eval))
    bfile.close()
#Correções: 
# Salvar metade da população para a prox GEN
# Fazer dataframe (geração, Cromossomos, score) exportar em .csv

    print('breakpoint')