import math
# интервал [-1:0]
def fun (x):
    return x**4 + 2 * x *x + 4* x + 1

def findXi(A, delta, i):
    return A + delta * i / N
print('Метод равномерного поиска. ЦФ: f(x) = x^4+2x^2+4x+1',)
print('Интервал: [-1:0]')
print('ex = 0.01, ey = 0.001 ')
print('N = 8')

A = -1
B = 0
N = 8
xi = []
fxi = []
ex = 0.01
ey = 0.001
a0, b0 = A, B
m=1
while(1):
    print('--------------Итерация №', m, '--------------')
    del0 = b0 - a0
    x0 = (a0 + b0) / 2
    print('a=', a0, 'b=', b0, 'del=', del0)
    for i in range (1,N):
        xi.append(findXi(a0, del0, i))
        fxi.append(fun(findXi(a0, del0, i)))
    print('Xi:', xi)
    print('f(Xi):', fxi)
    res = min(fxi)
    ind = fxi.index(res)
    a1 = xi[ind-1]
    b1 = xi[ind+1]
    del1 = b1 - a1
    x1 = xi[ind]
    print('min=', res, 'j=', x1)
    if (math.fabs(fun(x1)-fun(x0)) < ey) and (del1/2 < ex):
        print('Результат:')
        print('x* =', round(x1, 2), 'f* =', round(res, 3))
        break
    print('Условия остановки итерационного процесса не выполняются:')
    print('fun(x1)-fun(x0)=',math.fabs(fun(x1)-fun(x0)),'> ey')
    print('del/2', del1/2, '> ex')
    del0, a0, b0 = del1, a1, b1
    m = m+1

