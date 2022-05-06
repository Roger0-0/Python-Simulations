from random import uniform
import numpy as np
import matplotlib.pyplot as plt 
###OPTIONS###
C1=(0,0) #Center locations
C2=(1,1)
A1=2     #Major axi
A2=.5
B1=1     #Minor axi
B2=2
N=10000  #Monte-Carlo depth
###############

#Uses parametric form to draw ellipse. 
def DrawEllipse(center,a,b):
  u=center[0]
  v=center[1]
  t=np.linspace(0,2*np.pi,1000)
  x=u+a*np.cos(t)
  y=v+b*np.sin(t)
  plt.plot(x,y)
  return x,y

# Monte Carlo method to compute cross sectional area.
def MonteCarlo(n,x1,x2,y1,y2,c,ab):
  hits=0
  #Get box dimentions.
  all_x=np.concatenate((x1,x2))
  all_y=np.concatenate((y1,y2))
  minx,maxx=min(all_x),max(all_x)
  miny,maxy=min(all_y),max(all_y)
  A=abs((maxx-minx)*(maxy-miny))
  print('Area of box is',A)

  #Generate Random points
  for i in range(n):
    x=uniform(minx,maxx)
    y=uniform(miny,maxy)
    p=(x,y)
  #Create hit conditionals.
    if (x-c[0])**2/(ab[0]**2)+(y-c[1])**2/(ab[1]**2)<=1: #its in ellipse 1
      if (x-c[2])**2/(ab[2]**2)+(y-c[3])**2/(ab[3]**2)<=1:#its in ellipse 2
        plt.scatter(p[0],p[1],c='pink')
        hits+=1
  print(f'{hits} hits, with a hit probability of {hits/n}%')
  print(f'The cross-sectional area is {(hits/n)*A}')

def main():
  print("Hold you're horses I'm working on it.")
  x1,y1=DrawEllipse(C1,A1,B1)
  x2,y2=DrawEllipse(C2,A2,B2)
  centers=C1+C2
  ab=(A1,B1,A2,B2)
  MonteCarlo(N,x1,x2,y1,y2,centers,ab)
  plt.xlabel('x',size=15),plt.ylabel('y',size=15),plt.title('Cross Section of Two Ellipses',size=15)
  plt.grid()
  plt.show()
  
  
main()