float x;
float y;
void setup(){
  x = random(-1,1);
  y = random(-1,1);
  size(500,500);
}

void draw(){
  x = random(-1,1);
  float px = map(x, 1,-1,0,width);
  y = random(-1,1);
  float py = map(x, 1,-1,height,0);
  ellipse(px*sin(px), py, 10, 10);
  println(px*sin(px));
}
