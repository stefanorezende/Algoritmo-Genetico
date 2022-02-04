from numpy.random import rand
from numpy.random import randint
import os
import time
import shutil

def write_aelFunction(gen, pop):
    dirName = 'gen{}'
    filename = 'ind{}.ael'
    filename0 = 'ind0{}.ael'
    string1 = '\ndecl context = de_get_design_context_from_name("AEL_Python_lib:gen{}:layout");'
    string2 = '\nde_show_context_in_new_window(context);'
    string3 = "\nADS_drawCells (28, 28, {}]);\n"    

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
        f.write(string3.format(crostr))
        f.close()


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