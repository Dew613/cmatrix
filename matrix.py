import math


def print_matrix( matrix ):
    i=0
    while(i!=len(matrix)):
        print matrix[i]
        print " "
        i+=1

def ident( matrix ):
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[i])):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix
            
        
                
    

def scalar_mult( matrix, s ):
    for i in range(0, len(matrix)):
        for j in range (0, len(matrix[i])):
            matrix[i][j]= matrix[i][j]*s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    ans = new_matrix(len(m2[0]), len(m1))
    # go through row of m1
    for i in range(len(m1)):
       # go through coluns of m2
       for j in range(len(m2[0])):
           # go through row of m2
           for a in range(len(m2)):
               ans[i][j] += m1[i][a] * m2[a][j]
    return ans


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
