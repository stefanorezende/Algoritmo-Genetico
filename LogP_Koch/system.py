import pandas as pd
import numpy as np
from numpy.random import rand
from numpy.random import randint
import math
import os
import time
import shutil
import psutil

def encod_func (indv):
    Wsbin = ''.join([str(b) for b in indv[0:3]]) # 3 bits
    Ws = round(1.666+int(Wsbin,2)*0.333, 2)

    Lsbin = ''.join([str(b) for b in indv[3:7]]) # 4 bits
    Ls = 39.5+int(Lsbin,2)*0.5

    Lstubin = ''.join([str(b) for b in indv[7:11]]) # 4 bits
    Lstub = 10+int(Lstubin,2)

    # Degree
    deg1bin = ''.join([str(b) for b in indv[11:13]]) # 2 bits
    deg2bin = ''.join([str(b) for b in indv[13:15]]) # 2 bits
    deg3bin = ''.join([str(b) for b in indv[15:17]]) # 2 bits
    deg4bin = ''.join([str(b) for b in indv[17:19]]) # 2 bits
    deg5bin = ''.join([str(b) for b in indv[19:21]]) # 2 bits
    deg6bin = ''.join([str(b) for b in indv[21:23]]) # 2 bits

    deg1 = int(deg1bin,2)
    deg2 = int(deg2bin,2)
    deg3 = int(deg3bin,2)
    deg4 = int(deg4bin,2)
    deg5 = int(deg5bin,2)
    deg6 = int(deg6bin,2)

    Degree = '[%s, %s, %s, %s, %s, %s]' %(deg1, deg2, deg3, deg4, deg5, deg6)

    # Lmon
    Lmon1bin = ''.join([str(b) for b in indv[23:28]]) # 5 bits
    Lmon2bin = ''.join([str(b) for b in indv[28:33]]) # 5 bits
    Lmon3bin = ''.join([str(b) for b in indv[33:38]]) # 5 bits
    Lmon4bin = ''.join([str(b) for b in indv[38:43]]) # 5 bits
    Lmon5bin = ''.join([str(b) for b in indv[43:48]]) # 5 bits
    Lmon6bin = ''.join([str(b) for b in indv[48:53]]) # 5 bits

    Lmon1 = 10+int(Lmon1bin,2)*1.25
    Lmon2 = 10+int(Lmon2bin,2)*1.25
    Lmon3 = 10+int(Lmon3bin,2)*1.25
    Lmon4 = 10+int(Lmon4bin,2)*1.25
    Lmon5 = 10+int(Lmon5bin,2)*1.25
    Lmon6 = 10+int(Lmon6bin,2)*1.25

    Lmon = '[%s, %s, %s, %s, %s, %s]' %(Lmon1, Lmon2, Lmon3, Lmon4, Lmon5, Lmon6)

    # Ymon
    Ymon1bin = ''.join([str(b) for b in indv[53:58]]) # 5 bits
    Ymon2bin = ''.join([str(b) for b in indv[58:63]]) # 5 bits
    Ymon3bin = ''.join([str(b) for b in indv[63:68]]) # 5 bits
    Ymon4bin = ''.join([str(b) for b in indv[68:73]]) # 5 bits
    Ymon5bin = ''.join([str(b) for b in indv[73:78]]) # 5 bits
    Ymon6bin = ''.join([str(b) for b in indv[78:83]]) # 5 bits

    Ymon1 = round(Ls/3*math.ceil(1/2)-int(Ymon1bin,2)*Ls/96, 2)
    Ymon2 = round(Ls/3*math.ceil(2/2)-int(Ymon2bin,2)*Ls/96, 2)
    Ymon3 = round(Ls/3*math.ceil(3/2)-int(Ymon3bin,2)*Ls/96, 2)
    Ymon4 = round(Ls/3*math.ceil(4/2)-int(Ymon4bin,2)*Ls/96, 2)
    Ymon5 = round(Ls/3*math.ceil(5/2)-int(Ymon5bin,2)*Ls/96, 2)
    Ymon6 = round(Ls/3*math.ceil(6/2)-int(Ymon6bin,2)*Ls/96, 2)

    Ymon = '[%s, %s, %s, %s, %s, %s]' %(Ymon1, Ymon2, Ymon3, Ymon4, Ymon5, Ymon6)


    Subsbin = ''.join([str(b) for b in indv[83:85]])
    Subs = int(Subsbin,2)

    # print(Wsbin+Lsbin+Lstubin+deg1bin+deg2bin+deg3bin+deg4bin+deg5bin+deg6bin+Lmon1bin+Lmon2bin+Lmon3bin+Lmon4bin+Lmon5bin+Lmon6bin+Ymon1bin+Ymon2bin+Ymon3bin+Ymon4bin+Ymon5bin+Ymon6bin+Subsbin)

    callfStr = 'ADS_drawLogP(%s, %s, %s, %s, %s, %s, %s);' %(Ws, Ls, Lstub, Degree, Lmon, Ymon, Subs)
    return(callfStr)


def write_aelFunction(gen, pop):
    # Create target Directory if don't exist
    dirName = 'gen%s' %(gen)
    callf_arr = np.array([])
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print('Directory ' , dirName,  ' Created')
    else:    
        print('Directory ' , dirName,  ' already exists')

    for i in range(0,len(pop)):
        if i < 10:
            filename0 = 'gen%s\\indv0%s.ael' %(gen, i)
            shutil.copyfile('model.ael', filename0)
            f = open (filename0,"a+")
        else:
            filename = 'gen%s\\indv%s.ael' %(gen, i)
            shutil.copyfile('model.ael', filename)
            f = open (filename,"a+")
        
        callf = encod_func(pop[i])

        callf_arr = np.append(callf_arr, callf)

        f.write('\ndecl context = de_get_design_context_from_name("Koch_LogPer_lib:cell_1:layout"); \nde_show_context_in_new_window(context); \n%s' %(callf))
        f.close()

    return(callf_arr)


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def callAelCMD(gen):
    arqv = os.listdir('gen%s' %(gen))
    for fileael in arqv:
        enginerun = True
        print('CMD Command: ads -m gen%s\\%s' %(gen, fileael)) 
        os.system('ads -m gen%s\\%s' %(gen, fileael))               
        time.sleep(45)

        while enginerun == True:
            enginerun = checkIfProcessRunning('MomEngine.exe')
            time.sleep(10)            

        os.system(r'taskkill/im hpeesofde.exe /f')


def read_fitFunction():
    filename = 'C:\\Users\\stefa\\ADS_wrk\\Koch_LogPer_wrk\\data\\python\\5GfitFunction.txt'
    f = open(filename,'r')
    fl = f.read().splitlines() 
    scores = [float(item) for item in fl]    
    f.close()

    os.remove(filename)
    return (scores)


def write_df(temp, df, gen, pop, callf_arr,scores):   
    
    temp['gen'] = np.resize(['gen%s'%(gen)], len(temp))
    temp['indv'] = pop
    temp ['callf'] = callf_arr
    temp['scores'] = scores

    df = pd.concat([df, temp], ignore_index= True)

    return(df)