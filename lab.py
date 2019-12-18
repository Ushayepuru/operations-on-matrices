import numpy as np
A=np.array(input('enter a 2*2 matrix'));
B=np.array(input('enter a 2*2matrix'));
#operations on matix
a=np.add(A,B)
print "addition of two matrices\n",a
b=np.subtract(A,B)
print "subtraction of two matrices\n",b
c=np.divide(A,B)
print "division  of two matrices\n",c
d=np.multiply(A,B)
print "multiplication of two matrices\n",d
f=np.trace(A)
print "trace of  matrix A\n",f
g=np.trace(A)
print "trace of  matrix B\n",g
h=np.sqrt(A)
print "squareroot of two matrix A\n",h
i=np.dot(A,B)
print "dot product of two matrix A\n",i
#linear algebric operations
j=np.linalg.multi_dot(A)
print "dot product of the matrix A\n",j
k=np.linalg.matrix_power(A,5)
print "a square matrix to the power 5 A\n",k
l=np.linalg.cholesky(B)
print "cholesky decomposition of matrix B\n",l
m=np.linalg.eigvals(A)
print "eigenvalues of matrix A\n",m
n=np.linalg.det(B)
print "cross product of two matrix B\n",n
p=np.linalg.slogdet(A)
print "the sign and logarithm of matrix A\n",p
q=np.linalg.matrix_rank(A)
print "rank of the  matrix A\n",q
r=np.linalg.norm(B)
print "norm of the  matrix B\n",r
s=np.linalg.cond(A)
print "rank of the  matrix A\n",s
t=np.linalg.solve(A,B)
print "linear matrix eqation of the matrices A,B\n",t
w=np.linalg.inv(A)
print "inverse of the  matrix A\n",w
x=np.linalg.pinv(A)
print "pseudo inverse of the  matrix A\n",x





































