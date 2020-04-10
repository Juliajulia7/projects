a1=0.1 #меняем параметры
a2=0.50 
a3=0.80 
a4=1.20 

a11=a1*10 
a44=a4*10 

a=a1 
b=a4 

h=0.1 
h1=h*10 

n=(a44-a11)/h1-1 

N=(a44-a11)/h1+1 


p1=7 #меняем параметры 
p2=5 
p3=1 

q1=0 
q2=1 
q3=2 

Ua=0.4
Jb=-0.4
#Kb=0.7 
#Uc_b=2 

x=seq(from=a11,to=a44,by=h1) 
x=x/10 



f1=function(x){sqrt(1+x)} 
f2=function(x){7+exp(-x)} 
f3=function(x){0} 



K=matrix(nrow=n+2, ncol=3) 
M=matrix(nrow=n+2, ncol=3) 
F=c() 


for (j in 2:(n+1)){ 
  
  if (j*h < a2 && j>1 && j<(n+2)){ 
    Q1=q1 
    Q2=q1 
    P1=p1 
    P2=p1 
  } 
  
  if (j*h < a3 && j*h > a2 && j>1 && j<(n+2)){ 
    Q1=q2 
    Q2=q2 
    P1=p2 
    P2=p2 
  } 
  
  if (j*h > a3 && j>1 && j<(n+2)){ 
    Q1=q3 
    Q2=q3 
    P1=p3 
    P2=p3 
  } 
  
  if (j*h == a2 ){ 
    Q1=q1 
    Q2=q2 
    P1=p1 
    P2=p2 
  } 
  
  if (j*h == a3){ 
    Q1=q2 
    Q2=q3 
    P1=p2 
    P2=p3 
  } 
  #матрица массы(1,2,3 столбцы)
  M[j,1]=Q1*h/6 
  M[j,2]=(Q1+Q2)*h/3 
  M[j,3]=Q2*h/6 
  #матрица жесткости
  K[j,1]=-P1/h 
  K[j,2]=(P1+P2)/h 
  K[j,3]=-P2/h 
  
  
} 

#заполнение первой строки
M[1,2]=q1*h/3 
M[1,3]=q1*h/6 
K[1,2]=p1/h 
K[1,3]=-p1/h 


#заполнение последней строки
M[n+2,1]=q3*h/6 
M[n+2,2]=q3*h/3 
K[n+2,1]=-p3/h 
K[n+2,2]=p3/h 

#Функция "зубчик"
e1=function(z){(z-x[i-1])/(x[i]-x[i-1])} 

e2=function(z){(-z+x[i+1])/(x[i+1]-x[i])} 

e0=function(z){(x[2]-z)/(x[2]-x[1])} 

emax=function(z){(z-x[n-1])/(x[n+2]-x[n+1])} 

integral=function(f,a,b,n){ 
  h=(b-a)/n 
  x=seq(from=a, to=b, by=h) 
  y=f(x) 
  res=(b-a)/n*sum(y) 
  return(res) 
} 

i=2 
#заполняем вектор F
while (i < (n+2)){ 
  if(i < which(x==a2)) { 
    F1=function(z){f1(z)*e1(z)} 
    F2=function(z){f1(z)*e2(z)} 
  } 
  if(i > which(x==a2) && i < which(x==a3)){ 
    F1=function(z){f2(z)*e1(z)} 
    F2=function(z){f2(z)*e2(z)} 
  } 
  if(i > which(x==a3) && i < which(x==a4)){ 
    F1=function(z){f3(z)*e1(z)} 
    F2=function(z){f3(z)*e2(z)} 
  } 
  if(i == which(x==a2)){ 
    F1=function(z){f1(z)*e1(z)} 
    F2=function(z){f2(z)*e2(z)} 
  } 
  if(i == which(x==a3)){ 
    F1=function(z){f2(z)*e1(z)} 
    F2=function(z){f3(z)*e2(z)} 
  } 
  
  
  F[i] = integral(F1,x[i-1],x[i],10000)+integral(F2,x[i],x[i+1],10000) 
  
  i=i+1 
  
} 


F[1]=Ua 

F1=function(z){f3(z)*emax(z)} 
F[n+2]=integral(F1,x[n+1],x[n+2],10000)+Jb #меняем граничные условия(см.таблица 6)

al=c() 
bet=c() 
a=c() 
b=c() 
c=c() 



c[1]=0 
b[1]=1 

a[n+2]=K[n+2,1]+M[n+2,1] 
b[n+2]=K[n+2,2]+M[n+2,2] # меняется из-за типа граничных условий таблица 4

al[1]=-c[1]/b[1] 
bet[1]=F[1]/b[1] 

for (j in 2:(n+1)) 
{ 
  
  a[j]=K[j,1]+M[j,1] 
  b[j]=K[j,2]+M[j,2] 
  c[j]=K[j,3]+M[j,3] 
  al[j]=-(c[j])/(a[j]*al[j-1]+b[j]) 
  bet[j]=(F[j]-a[j]*bet[j-1])/(a[j]*al[j-1]+b[j]) 
} 

u=c() 

u[n+2]=(F[n+2]-a[n+2]*bet[n+1])/(a[n+2]*al[n+1]+b[n+2]) 

j=n+1 
while (j >= 1) 
{ 
  u[j]=al[j]*u[j+1]+bet[j] 
  j=j-1 
} 

plot(x,u)