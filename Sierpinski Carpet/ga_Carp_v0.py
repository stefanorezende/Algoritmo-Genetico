from numpy.random import rand
from numpy.random import randint
import os
import time
import shutil

n_pop = 10

def population (n_pop):
    pop=[]
    for i in range(n_pop):

        L = randint(0, 121)
        Ldec = randint (0,100)

        W = randint(0,30)
        Wdec = randint (0,100)

        degree = randint(0, 5 if W > 100 and L > 100 else 4)

        ind = [L, Ldec, W, Wdec, degree]

        pop.append(ind)
    
    return (pop)

def write_aelFunction(gen, pop):
    dirName = 'gen{}'
    filename = 'ind{}.ael'
    filename0 = 'ind0{}.ael'
    string1 = '\ndecl context = de_get_design_context_from_name("Sierpinski_Carpet_AEL_Python_lib:gen{}:layout");'
    string2 = '\nde_show_context_in_new_window(context);'
    string3 = "\nADS_drawSierpCapet ({}, {}, {});\n"    

    # shutil.rmtree(dirName.format(gen))

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
        
        Lstr = str(pop[i][0]+0.1*pop[i][1])
        Wstr = str(pop[i][2]+0.1*pop[i][3])
        f.write(string1.format(gen))
        f.write(string2)
        f.write(string3.format(Lstr,Wstr,pop[i][4]))
        
        f.close()

def callAelCMD (gen, fileael):
    
    comm = 'ads -m gen{}\\{}'
    # for fileael in arqv:
    print(comm.format(gen,fileael))
    os.system(comm.format(gen,fileael))        
    # os.system(r'ads -m C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\AEL\\ADS_layout_drawCells_v2.ael')
    time.sleep(10)
    os.system(r'taskkill/im hpeesofde.exe /f')

def checkDB (pop, gen):
    datbas = open ('Database.txt', 'r')
    db_lin = datbas.read().splitlines()
    datbas.close()

    db_fit = [db_lin[k].rsplit(';',1)[1] for k in range(len(db_lin))]
    db_pop = [db_lin[k].rsplit(';',1)[0] for k in range(len(db_lin))]

    arqv = os.listdir('gen{}'.format(gen))

    for i in range(len(pop)):
        valid = False
        for j in range (len(db_lin)):            
            if str(pop[i]) == db_pop [j]: valid = True                
        if(valid == True):       
            fit = open('C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\python\\5GfitFunction{}.txt'.format(gen), 'a+')
            fit.write('\n{}'.format(db_fit[j]))
            fit.close()
        else:
            callAelCMD(gen, arqv[i])

def read_fitFunction(gen):
    filename = 'C:\\Users\\stefa\\ADS_wrk\\AEL_Python_wrk\\data\\python\\5GfitFunction{}.txt'
    f = open(filename.format(gen),'r')
    fl = f.read().splitlines() 
    scores = [float(item) for item in fl]
    return (scores)

def saveDB (pop,scores):
    datbas = open ('Database.txt', 'r')
    db_lin = datbas.read().splitlines()
    datbas.close()
    for k in range(len(db_lin)):
        db_lin[k] = db_lin[k].rsplit(';',1)[0]

    datbas = open ('Database.txt', 'a+')
    # datbas.write ('[0, 0, 0, 0, 0];0.0\n ')
    for i in range(len(pop)):
        valid = False
        for j in range (len(db_lin)):            
            if str(pop[i]) != db_lin [j]: valid = True                
        if(valid == True): datbas.write ('\n{};{} '.format(pop[i],scores[i])) 
    datbas.close()

def genetic_algorithm (n_gen, target, n_pop):
    pop = population(n_pop)
    scores = [0 for i in range(n_pop)]
    best, best_eval = 0, 0

    for gen in range(n_gen):
        write_aelFunction(gen, pop)
        checkDB (pop, gen)
        scores = read_fitFunction(gen)
        saveDB(pop, scores)

    return (pop)


if __name__ == "__main__":
    target = 100
    n_gen = 1
    n_pop = 3

    pop = genetic_algorithm(n_gen, target, n_pop)   


print('breakpoint')