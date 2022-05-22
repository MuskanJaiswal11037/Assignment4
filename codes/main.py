

import numpy as np
from numpy import random as RN
from matplotlib import pyplot as plt
from pconst import const

''' Ques- In a meeting, 70% of the members favour and 30% oppose a certain proposal. A member is
 selected at random and we take X=0 if he opposed, and X=1 if he is in favour. Find E(X) and Var(X).

Ans-
Let x be the random variable such that
    x=0 , if the member opposes a certain proposal
    x=1 , if the member favours a certain proposal 
      
    Let E(x) =E, E(x^2)=E2 and Var(X)=V   
         
           '''



# So , The Theoretical probabilities
pr =  [7/10,3/10]
N=100
E=0
E2=0
for x in [0,1]:
    E=E+pr[x]*x
p=x**2
for x in [0,1]:
    E2=E2+pr[x]*p
V=E2-E**2
print("Expected value is : ", E)
print(" Variance is equal to ",V)



# Let x take any value from 0 to 9 inclusive over the size N ,
t = RN.randint(0, 10,size=N)
# and if x = {3,4,5,6,7,8,9} , then we shall take the member to favour the proposal.
# and if x = {0,1,2} , then we shall take the member to oppose the favour.

#Finding the number of numbers which are greater than or equal to 3.
x_0 = np.count_nonzero(t>=3)

#So ,number of numbers such that x=0,x=1,x=2 are
x_1 = N - x_0






print("Theoretical Probabilities:", pr[0], pr[1])
print("Practical Probabilities:", x_0/N, x_1/N)
width = 0.2
y1 = [pr[0],pr[1]]
x2 = [0,1]
y2 = [x_0/N,x_1/N]
plt.stem(x2, y1 ,linefmt='black' ,markerfmt = 'D',label = 'Theoretical')
plt.stem(x2, y2 ,linefmt= 'grey' , label = 'Experimental')
plt.xlabel('Outcomes')
plt.ylabel('Probability')
#x3 = [1+width/2,2+width/2,3+width/2,4+width/2,5+width/2,6+width/2,]
#plt.xticks(x3,x)
plt.legend(loc = 9)
plt.show()
plt.savefig('figures/plot.png')
