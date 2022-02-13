from numpy.random import randint
import math
import os

n_bits = 85
indv = randint(0,2,n_bits).tolist()


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

callf = 'ADS_drawLogP(%s, %s, %s, %s, %s, %s, %s);' %(Ws, Ls, Lstub, Degree, Lmon, Ymon, Subs)

print(callf)
print('breakpoint')

f = open ('model.ael','a+')
f.write('\n%s'%(callf))
f.close()

os.system('ads -m model.ael')

       