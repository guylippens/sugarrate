import numpy as np
import argparse


def regulate(output_dir='.', n=5000, s=0.001, l=0.4, t=3):
    """generate 3 files results. 

    Args:
        output_dir (str): directory path where to write results
        n (int): number of molecules
        s (float): small size molecules probability
        l (float): large size molecules probability
        t (int): minimal length to transit from short to long
    """
    i = 0
    aa = np.ones(n)  # sucrose molecules are both donors and acceptors
    xx = np.ones(n)  # Counter for the donors
    c = 0  # consumption of sucrose start -  will be updated during the algorithm
    outfile = open(output_dir+'/AutoconsumptionLength' +
                   '_'+str(l)+'_'+str(s)+'_'+str(n), 'w')
    r = n  # molecules available for elongation – will be updated during the algorithm
    while c < n:
        i = i+1
        bb = np.nonzero(aa)
        cc = bb[0]
        a = np.random.random(1)
        # index of the random molecule selected for elongation
        b = np.random.randint(len(cc))
    # selected from the entire list except for the cleaved molecules
        q = l
        if aa[cc[b]] < t:
            q = s
        if a < q:  # If true, the molecule becomes elongated by 1
            aa[cc[b]] = aa[cc[b]]+1
            xx = np.where(aa == 1)[0]
            # but this implies also that a sucrose molecule has been cleaved
            aa[xx[0]] = 0
            r = r-1
        c = n-r
        if i % 1000 == 0:
            e = str(c)
            m = int(np.max(aa))
            print('Cycle = ', i, 'Consumption = ', c, 'Max distribution = ', m)
            outfile.write(e+"\n")
        if (len(xx) < 0.1*n):  # We stop at 10% of monomers
            c = n
    print('Number of cycles = ', i)
    m = int(np.max(aa))
    print('Maximum of distribution = ', m)  # Used to construct a histogram
    kk = np.arange(m)  # array from 0 to (m-1)
    yy = np.histogram(aa, bins=kk)
    zz = yy[0]
    outfile = open(output_dir+'/AutohistogramLength' +
                   '_'+str(l)+'_'+str(s)+'_'+str(n), 'w')
    i = 0
    while i < m-1:
        a = str(zz[i])
        outfile.write(a+"\n")
        i = i+1
    outfile.close()
    outfile = open(output_dir+'/AutohistogramLength_glucose'+'_' +
                   str(l)+'_'+str(s)+'_'+str(n), 'w')
    i = 0
    while i < m-1:
        a = str(zz[i]*i)
        outfile.write(a+"\n")
        i = i+1
    outfile.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument(
        "output_dir", help="dir path where to write the result files ")
    parser.add_argument("-n", type=int, help="number of molecules")
    parser.add_argument(
        "-s", type=float, help="small size molecules probability")
    parser.add_argument(
        "-l", type=float, help="large size molecules probability")
    parser.add_argument(
        "-t", type=int, help="minimal length to transit from short to long")

    args = parser.parse_args()

    regulate(**vars(args))
