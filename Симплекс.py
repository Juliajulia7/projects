import math
from copy import copy, deepcopy
from tabulate import tabulate

ex = 0.01
ey = 0.001
def fun2(x1, x2):
    return 2 * (x1 - 4)**2 + (x2 - 6)**2

# def fun2(x1, x2):
#     return (x1 - x2)**2 + (x1 * x1 -x2 + 2)**2

p0 = (math.sqrt(3) + 1) / (2 * math.sqrt(2))
g0 = (math.sqrt(3) - 1) / (2 * math.sqrt(2))
delt = 1
x01 = 0
x02 = 0
al = 0.5
table = []
headers = ['k', 'del k', 'Vk', 'f(Vk)', '[p,m]', 'V kp, f(V kp)', 'xk', 'f(xk)', '[ ||xk+1  - xk||, |fk+1 - fk| ]' ]
def matV (x1, x2, p, g):
    matr = [[x1, x2], [x1 + p, x2 + g], [x1 + g, x2 + p]]
    return matr
def findX3(matrix):
    res = [0, 0]
    res[0] = (matrix[0][0]/3 + matrix[1][0]/3 + matrix[2][0]/3)
    res[1] = (matrix[0][1]/3 + matrix[1][1]/3 + matrix[2][1]/3)
    return res

def findX(matrix):
    res = [0, 0]
    res[0] = (matrix[0][0] + matrix[1][0] + matrix[2][0])
    res[1] = (matrix[0][1] + matrix[1][1] + matrix[2][1])
    return res

def matVl(f1, f2, f3):
    Vl = []
    Vl[0] = f1[0]+f2[0]+f3[0]
    Vl[1] = f1[1]+f2[1]+f3[1]
    return Vl
def round1(matr):
    matr1=deepcopy(matr)
    for i in range (0,len(matr)):
        for j in range (0, len(matr[0])):
           matr1[i][j]=round(matr[i][j], 3)
    return matr1

def round2(matr):
    matr1=deepcopy(matr)
    for i in range (0,len(matr)):
        matr1[i]=round(matr[i], 3)
    return matr1


p1 = p0 * delt
g1 = g0 * delt
x1, x2 = x01, x02
V1 = matV(x1, x2, p1, g1)
xl = findX3(V1)
fVGen = [0, 0, 0]
fxl = fun2(xl[0], xl[1])
m = 1
while(1):
    fVGen[0] = fun2(V1[0][0], V1[0][1])
    fVGen[1] = fun2(V1[1][0], V1[1][1])
    fVGen[2] = fun2(V1[2][0], V1[2][1])
    max1 = max(fVGen)
    min1 = min(fVGen)
    indx = fVGen.index(max1)
    indxMin = fVGen.index(min1)
    V12 = deepcopy(V1)
    for j, _ in enumerate(V12[indx][:]):
        V12[indx][j] *=  -1
    V02 = findX(V12)
    if(fun2(V02[0],V02[1])>max1):
        delt = delt * al
        for i in range (3):
            for b in range (2):
                V12[i][b] = al * V1[i][b] + (1- al) * V1[indxMin][b]
                p1 = p0 * delt
                g1 = g0 * delt
    else:
        V12[indx][:] =  V02
    xnew = findX3(V12)
    fxnex= fun2(xnew[0], xnew[1])
    normX = math.sqrt((xnew[0]-xl[0])**2 + (xnew[1]-xl[1])**2)
    vecView = [m, delt,  round1(V1), [round(fVGen[0], 3), round(fVGen[1], 3), round(fVGen[2], 3)], [indx+1, indxMin+1], [round2(V02),round(fun2(V02[0], V02[1]),3)], round2(xl), round(fxl,3),
               [round(normX,3), round(math.fabs(fxnex - fxl),3)]]
    table.append(vecView)
    if ((normX < ex) and (math.fabs(fxnex - fxl)<ey)):
        print(tabulate(table, headers, tablefmt="github"))
        break
    V1 = V12
    fxl = fxnex
    xl=xnew
    xl = xnew
    m = m+1
