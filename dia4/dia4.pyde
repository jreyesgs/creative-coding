def gradosRadianes(g):
    return (g*(PI*2))/360
    
def pintaQueso(x, y, w, h, cuadrante):
    inicio = 360-(90*cuadrante)
    arc(x, y, w, h, gradosRadianes(inicio), gradosRadianes(inicio+90), PIE)

i = 1

def setup():
    size(1920,1080)
    background(255)
    #fill(200+random(55),200,200+random(55),50+random(10))
    noStroke()
    for h in range(width/40):
        for w in range(height/40):
            fill(200+random(55),200,200+random(55),random(80,100))
            pintaQueso(40*h, 40*w, 80, 80, int(random(4)))
    
            
    
def draw():
    #saveFrame("line-######.png");
    pass

              
