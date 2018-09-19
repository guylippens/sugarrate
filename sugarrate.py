import os
os.chdir("U:\MC_DSRM\Papier_W624A\ReactionRate")
import pandas
import numpy as pd
i = 0
n = 50000  # Initial sucrose concentration
aa = pd.ones(n)  # sucrose molecules are both donors and acceptors
yy = pd.ones(n)  # Counter for the donors
t = 3  # minimal length to transit from short to long status
l = 0.4  # Probability for long chains
s = 0.001  # Probability for short chains
c = 0  # consumption of sucrose – will be updated during the algorithm
outfile = open('AutoconsumptionLength'+'_'+str(l)+'_'+str(s)+'_'+str(n), 'w')
r = n  # molecules available for elongation – will be updated during the algorithm
while c < n:
    i = i+1
    bb = pd.nonzero(aa)
    cc = bb[0]
    a = pd.random.random(1)
    # index of the random molecule selected for elongation
    b = pd.random.randint(len(cc))
# selected from the entire list except for the cleaved molecules
    q = l
    if aa[cc[b]] < t:
        q = s
    if a < q:  # If true, the molecule becomes elongated by 1
        aa[cc[b]] = aa[cc[b]]+1
        xx = pd.where(aa == 1)
        yy = xx[0]
        aa[yy[0]] = 0  # but this implies also that a sucrose molecule has been cleaved
        r = r-1
    c = n-r
    if i % 1000 == 0:
        e = str(c)
        m = int(pd.max(aa))
        print('Cycle = ', i, 'Consumption = ', c, 'Max distribution = ', m)
        outfile.write(e+"\n")
    if (len(yy) < 0.1*n):  # We stop at 10% of monomers
        c = n
print('Number of cycles = ', i)
m = int(pd.max(aa))
print('Maximum of distribution = ', m)  # Used to construct a histogram
kk = pd.arange(m)  # array from 0 to (m-1)
yy = pd.histogram(aa, bins=kk)
zz = yy[0]
outfile = open('AutohistogramLenght'+'_'+str(l)+'_'+str(s)+'_'+str(n), 'w')
i = 1
while i < m-1:
    a = str(zz[i])
    outfile.write(a+"\n")
    i = i+1
outfile.close()
outfile = open('AutohistogramLength_glucose'+'_' +
               str(l)+'_'+str(s)+'_'+str(n), 'w')
i = 1
while i < m-1:
    a = str(zz[i]*i)
    outfile.write(a+"\n")
    i = i+1
outfile.close()
