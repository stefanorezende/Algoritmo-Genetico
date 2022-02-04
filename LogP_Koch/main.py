from numpy.random import rand
from numpy.random import randint
import ga

if __name__ == "__main__":
    n_gen = 8
    n_pop = 20
    n_cell = 16
    r_cross = 0.9
    r_mut = 1.0/float(n_cell)

    best, best_eval = ga.genetic_algorithm(n_gen, n_pop, n_cell, r_cross, r_mut)

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