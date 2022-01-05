# n_pop = 20
# n_gen = 3
# scores = [0 for i in range(n_pop)]

    
# for gen in range(n_gen):
#     if(gen != 0): scores = [10 for i in range(n_pop)]
#     print(scores)

# import shutil
# import os
# dirName = 'v1\\test'
# # Create target Directory if don't exist
# if not os.path.exists(dirName):
#     os.mkdir(dirName)
#     print("Directory " , dirName ,  " Created ")
# else:    
#     print("Directory " , dirName ,  " already exists")


# shutil.copyfile('C:\\Users\\stefa\\Desktop\\Python\\Algoritmo Genetico\\v1\\gen0\\ind0.ael', 'C:\\Users\\stefa\\Desktop\\Python\\Algoritmo Genetico\\v1\\test\\test.ael')
# # os.rename("textfile.txt", "newfile.txt")

str1 = '[1, 2, 3]'
n = [1, 2, 4]


# if (str(n)!= str1):
#     print('triste')
# else:
#     print ('alegre')

import os
arqv = os.listdir('gen0')
print(arqv)