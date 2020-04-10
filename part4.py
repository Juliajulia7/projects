

R = [ [0,1,1,1,0,0,0,0],[1,0,1,0,1,0,0,0],[1,1,0,1,1,0,0,0],
 [1,0,1,0,1,0,1,1],[0,1,1,1,0,1,1,0],[0,0,0,0,1,0,1,1],
 [0,0,0,1,1,1,0,1],[0,0,0,1,0,1,1,0]]

print(R[4][2])
print(R[1])
print(len(R[2]))
print(len(R))

def voisiness(i,j, R):
    if R[i][j] == 1 : return True
    else: return False

print(voisiness(3,0,R))
print(voisiness(3,5 ,R))

def list_voisiness(i, R):
    temp = []
    for k in range (len(R[i])):
        if R[i][k]==1: temp.append(k)
    return temp

def degre(i, R):
    return len(list_voisiness(i,R))

print(list_voisiness(3, R))
print(degre(3,R))
print(degre(0,R))
print(degre(2,R))




def list_degres(R):
    list=[]
    for j in range (len(R)):
        k=(j, degre(j,R))
        list.append(k)
    return list

def tri_degres(D):
    for i in range(len(R)):
        for j in range (i+1, len(D)):
            if D[i][1] < D[j][1]:
                D[i], D[j] = D[j], D[i]
    return D

print(tri_degres(list_degres(R)))

def tri_villes(R):
    list = []
    D=tri_degres(list_degres(R))
    for i in range (len(D)):
        list.append(D[i][0])
    return list

print( tri_villes(R))

def premier_entier(L):
    i=0
    k=3
    while(k!=0):
       if not (i in L):
        k=0
        return i
       i=i+1

print(premier_entier([0,0,3,1,0,1,0,0]))

def couleurs_voisines(k, C, R):
    list=[]
    for i in range (len(R)):
        if(R[k][i]!=0):
            list.append(C[i])
    return list

print(couleurs_voisines(4,[0,0,0,1,0,0,0,0], R))
print(couleurs_voisines(2,[0,0,0,1,2,0,0,0], R))
print(couleurs_voisines(6,[0,0,3,1,2,0,0,0], R))
print(couleurs_voisines(0,[0,0,3,1,2,0,3,0], R))

def couleurs_villes(R):
    V=tri_villes(R)
    C=[0]*len(V)
    for i in V:
        for j in range (len(R[i])):
            if R[i][j]!=0 and C[i]==0 and C[j]==0:
                C[j]=premier_entier(couleurs_voisines(i,C, R))
                C[j] = premier_entier(couleurs_voisines(j, C, R))
    return C

print(couleurs_villes(R))

def chemin_valide(T,R):
    if len(T)>2:
        T=list(T)
        for i in range(len(T)-1):
            if (R[T[i]][T[i+1]]!=1): return False
    return True

print(chemin_valide((2,0,1,4,3),R))
print(chemin_valide((7,6,4,5,6,3,4),R))
print(chemin_valide((3,1,4,7),R))

def chemin_simple(T):
    T1= list(set(T))
    if len(T)==len(T1):
        return True
    return False

print(chemin_simple((1,2,3)))

import numpy as np
import networkx as nx



def find_all_paths(G, start, end, path=[]):

    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in set(G.neighbors(start)) - set(path):
        paths.extend(find_all_paths(G, node, end, path))
    return paths


def liste_chemins(i,j,R):
    A = np.array(R)
    G = nx.DiGraph(A)
    return find_all_paths(G,i,j)



print((liste_chemins(1,5,R)))

def pc_chemins(i,j,R):
    list=[]
    listM=[]
    M=liste_chemins(i,j,R)
    for l in range (len(M)):
        list.append(len(M[l]))
    minE=min(list)
    for k in range (len(M)):
        if len(M[k])==minE:
            listM.append(M[k])
    return listM
#
print(pc_chemins(0,7,R))

def product_matriciel(A,B):
    return [ [ sum(map(lambda x: x[0] * x[1], zip(A[i], [c[j] for c in B]))) for j in range(len(B[0])) ] for i in range(len(A)) ]

print(product_matriciel([[1,2,1],[0,1,2]], [[1,0],[0,1],[1,1]]))


def Multiply(array_one, array_two, n):
    c = [[0]*len(array_one[0]) for i in range(len(array_one))]
    for i in range(n):
        for j in range(n):
            c[i][j] = sum(array_one[i][k]*array_two[k][j] for k in range(n))
    return c

def Power(array, n, y):
    if y == 0:
        return np.eye(len(array))
    if (y % 2) == 1:
        return Multiply(Power(array, n, y - 1 ), array, n)
    else:
        array = Power(array, n, y / 2)
        return Multiply(array, array, n)

def puissance(R,n):
    return Power(R, n, len(R))

print(puissance(R,5))

