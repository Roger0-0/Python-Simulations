import matplotlib.pyplot as plt 
from numpy import cos,sin,sqrt,pi,linspace
from random import uniform #random float in range (a,b)

#constants(dont change will break get_pie function)
BOX = 2
RADIUS = 1
STEPS = 1000
MAX_DOTS = 100000

#collects parametric form for a circle.
def get_circle():
    t = linspace(0,2*pi,STEPS)
    x = RADIUS * cos(t)
    y = RADIUS * sin(t)
    
    return x,y

#collects the dots and determines if dot is inside circle (hit)
def get_dots():
    xdots = []
    ydots = []
    hits = {'xhits':[],'yhits':[]}
    for i in range(0,MAX_DOTS):
        xdot = uniform(-BOX/2,BOX/2)
        ydot = uniform(-BOX/2,BOX/2)
        magnitude = sqrt(xdot**2 + ydot**2)
        if magnitude <= RADIUS:
            hits['xhits'].append(xdot)
            hits['yhits'].append(ydot)
        xdots.append(xdot)
        ydots.append(ydot)

    return xdots,ydots,hits

def get_pie(hits):
    box_area = BOX**2
    total_hits = len(hits['xhits'])
    pie = box_area * total_hits / MAX_DOTS
    return pie
    
    

def main():
    x,y = get_circle()
    xdots,ydots,hits = get_dots()
    pie = get_pie(hits)
    plt.plot(x,y)
    plt.scatter(xdots,ydots,color='blue')
    plt.scatter(hits['xhits'],hits['yhits'],color='green',label=fr'pi $\approxeq$ {pie}'.format(pie))
    plt.legend()
    plt.show()
    print(pie)

main()
