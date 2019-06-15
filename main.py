import sys
#import numpy as np
def print_mat(A,n):
    for i in range (0,n):
        print(A[i])
def ordem_multiplicacao(n,p):
    print (p)
    print("n= "+str(n))
    n = abs(n)
    #A = np.reshape(n,n)
    m = []
    s = []

    for i in range(0, n):
        m.append([])
        s.append([])
        for j in range(0, n):
            s[i].append(0)
            if i<j:
                m[i].append(0)
            else:
                m[i].append(0)
    print_mat(m,n)
    for l in range(1,n):
        print("L = {} ".format(l+1))

        for i in range(0,n-l):
            j = l+i
            m[i][j]= sys.maxsize
            print("I = {} ,j = {}".format(i+1,j+1))
            k = i

            while  (k < j) :

                q = m[i][k] + m[k+1][j] + ( p[i] * p[k+1] * p[j+1] )
                print("k = {} q={}+{}+({}*{}*{})= {}".format(k+1,m[i][k] , m[k+1][j] , p[i] , p[k+1] , p[j+1],q))
                if (q < m[i][j]):
                    m[i][j]=q
                    #m[j][i] = k+1
                    s[i][j] = k+1
                k = k +1
        print_mat(m, n)
    return m,s
    pass



def main(*args, **kwargs):
    n = 6
    p = [20,10,7,12,30,10,20]
    print(n)

    m,s=ordem_multiplicacao(n,p)
    print ("matriz M :")
    print_mat(m,n)
    print("matriz S :")
    print_mat(s, n)

    pass

if __name__ =="__main__":
    main()