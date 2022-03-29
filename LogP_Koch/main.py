from numpy.random import rand
from numpy.random import randint
from ga import genetic_algorithm
import time

if __name__ == "__main__":
    start_time = time.time()

    n_gen = 10
    n_pop = 4   # Must be an even integer
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
    rsecs= time.time() - start_time

    f = open('df_gens.csv','a+')
    f.write('\nRunning Time: %s:%s:%s hours' %(round(rsecs/3600), round(rsecs%3600/60), round(rsecs%60,3)))
    f.close()

    print('breakpoint')
