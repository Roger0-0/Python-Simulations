def Buffons_Needle(n,output):
  from random import random,uniform
  import math
  import matplotlib.pyplot as plt
  import numpy as np
  ###Constants#############
  l=0.5#length of needle.
  nl=n #number of needles.
  t=1 #width inbetween slits (should be 2*l for best results).
  h=5 #height of slits.
  ns=5 #number of slits.
  m=t/5 # x margin for needle generation.
  err=0.034505 #accepted error in when checking for hits.
  #########################
  hits=0
  # Generate slits.
  slits=[]
  for i in range(0,ns*t+1,t):
    s=(np.linspace(i,i,h+1),np.arange(0,h+1))# slit 
    slits.append(s)
    if output==True:
      plt.plot(s[0],s[1])
  # Generate needles.
  for j in range (nl):
    x1=uniform(-m,ns*t-m)
    y1=(h-1)*random()
    x2=uniform(x1,l+x1)# x2 <= l+x1 so the term under radical is positive.
    foo=random()
    # if else accounts for +- sqrt
    if foo>1/2:
      y2=y1+np.sqrt(l**2-(x2-x1)**2) #distance formula solved for y2
    else:
      y2=y1-np.sqrt(l**2-(x2-x1)**2)
    
    x=[x1,x2]
    y=[y1,y2]
    count=0
    for g in range(len(slits)):
      check=slits[g][0][0]
      if x2>=check-err and x1<=check+err:
        if output==True:
          z=plt.plot(x,y,c='red')
        hits+=1
        break
      count+=1
      if x1>=check-err and x2<=check+err:
        if output==True:
          z=plt.plot(x,y,c='red')
        hits+=1
        break
      if count==int(len(slits)):
        if output==True:
          z=plt.plot(x,y,c='black')
        break

  #Data
  P=hits/nl
  pi=(2*l)/(t*P) 
  if output==True:
    P_theory=(2*l)/(np.pi*t)
    print(100*P,'% of needles hit the mark')
    print(100*P_theory,'% of needles should have hit according to theory')
    print(100*P_theory-100*P,'% error')
    plt.title(f'Buffons Neddle simulation for {n} needles')
    plt.show()
  print(f'pi is estimated to be {pi}')

Buffons_Needle(10000,True)