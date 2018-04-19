def pointCircle(ra, angle, left, top):
    y = ra * sin(angle) + top;
    x = ra * cos(angle) + left;
    return {"_x": x, "_y": y};

def distancia(x1,y1,x2,y2):
    return sqrt(pow((x2-x1),2)+pow((y2-y1),2))

class Box:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.w = 30
        self.h = 30

    def update(self):
        self.drawBox(self.x,self.y)
        
    def drawBox(self, x, y):
        xc = x + self.w/2 
        yc = y + self.h/2 
        line(self.x + self.w/2, self.y + self.h/2, x+15, y+15)
        fill(255)
        rect(x, y, self.w, self.h)
        fill(0)
        ellipse(xc, yc, 3, 3)

pila = []
for i in range(10):
    for f in range(10):
        pila.append(Box(30*i,30*f))
    



def setup():
    size(300,300)
    
def draw():
    background(255,255,255,80)
    for p in pila:
        p.drawBox(mouseX,mouseY)
    saveFrame("frames/####.jpg")
        
    
    #c.update(random(300),random(300))
