import numpy as np
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

def distance(x1,x2,y1,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5
	
class swarm:
    def __init__(self):
        self.x = np.random.rand()*50
        self.y = np.random.rand()*50
        self.status = 1
		
dweebs = [0 for b in range (200)]
bullies = [0 for b in range (25)]
for i in range (len(dweebs)):
    dweebs[i] = swarm()
for i in range (len(bullies)):
	bullies[i] = swarm()

for t in range(720):
    for i in range (len(dweebs)):
        if(dweebs[i].status == 1):
		    for j in range(len(bullies)):
			    if (bullies[j].x-1 <= dweebs[i].x <= bullies[j].x+1 and bullies[j].y-1 <= dweebs[i].y <= bullies[j].y+1):
				    dweebs[i].status = 0
        if(dweebs[i].status == 1):
            cj = 0
            d = 100
            for j in range(len(bullies)):
                if(d > distance(dweebs[i].x,bullies[j].x,dweebs[i].y,bullies[j].y)):
                    d = distance(dweebs[i].x,bullies[j].x,dweebs[i].y,bullies[j].y)
                    cj = j
            d = distance(dweebs[i].x,bullies[cj].x,dweebs[i].y,bullies[cj].y)
            rr = np.random.rand()*100
            if(rr<=25):
                rot = np.math.atan2(bullies[cj].y - dweebs[i].y,bullies[cj].x - dweebs[i].x) + np.random.rand()*4-2
            else:
                rot = np.math.atan2(bullies[cj].y - dweebs[i].y,bullies[cj].x - dweebs[i].x)
            if(dweebs[i].x - np.math.cos(rot) < 50 and dweebs[i].x - np.math.cos(rot) > 0):
                dweebs[i].x -= np.math.cos(rot)
            if(dweebs[i].y - np.math.sin(rot) < 50 and dweebs[i].y - np.math.sin(rot) > 0):
                dweebs[i].y -= np.math.sin(rot)
    for i in range (len(bullies)):
        cd = 0
        db = 100
        for j in range(len(dweebs)):
            if(dweebs[j].status == 1):
                if(db > distance(bullies[i].x,dweebs[j].x,bullies[i].y,dweebs[j].y)):
                    db = distance(bullies[i].x,dweebs[j].x,bullies[i].y,dweebs[j].y)
                    cd = j
        db = distance(bullies[i].x,dweebs[cd].x,bullies[i].y,dweebs[cd].y)
        rot = np.math.atan2(dweebs[cd].y - bullies[i].y,dweebs[cd].x - bullies[i].x)
        if(bullies[i].x + np.math.cos(rot) < 50 and bullies[i].x + np.math.cos(rot) > 0):
		    bullies[i].x += np.math.cos(rot)
        if(bullies[i].y + np.math.sin(rot) < 50 and bullies[i].y + np.math.cos(rot) > 0):
            bullies[i].y += np.math.sin(rot)		
    fig = plt.figure()
    plt.gca().set_xlim([0,50])
    plt.gca().set_ylim([0,50])
    for i in range(len(dweebs)):
	    if(dweebs[i].status == 1):
	        plt.plot(dweebs[i].x, dweebs[i].y, 'go')

    for j in range(len(bullies)):	
        plt.plot(bullies[j].x, bullies[j].y, 'ro')
    plt.title('{0:03d}'.format(t))
    filename = 'img{0:03d}.png'.format(t)
    plt.savefig(filename, bbox_inches='tight')
    plt.close(fig)
