m=y.shape[0]
print(m)
on=np.ones((m,1))
x=np.hstack((on,x))
theta=np.zeros((x.shape[1],1))
print(theta)
h=np.zeros((m,1))
def lostfuntion(theta):
    J=1/(2*m)*np.dot((np.dot(x,theta)-y).T,np.dot(x,theta)-y)
    return J
def h(x):    
    return np.dot(x,theta)
print(x)
print(theta)
def grad(alpha,nn):
    for k in range(nn):
        for j in range(theta.shape[0]):
            sum=0
            for i in range(m):
                sum+=(h(x[i,:])-y[i])*x[i][j]
            theta[j]=theta[j]-alpha/m*sum
        print(theta,k)

s=int(input("Learning frequency"))
a=float(input("Learning rate"))
grad(a,s)
#print(theta)
plt.plot(x[:,1],np.dot(x,theta))    
plt.scatter(x[:,1],y)
plt.show()  
