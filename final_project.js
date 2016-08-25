import Math
// Global variables
int X, Y;
int nX, nY;
int bX, bY;
int delay = 10;
int points;
var direction;
var end;
color backgroundCol;
color ballCol;
color ballLine;
color paddleCol;
color paddleLine;
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Setup the Processing Canvas
void setup(){
  size( 700, 500 );
  strokeWeight( 4 );
  frameRate(50);
  X = width / 2;
  Y = 450;
  nX = X;
  nY = Y;
  bY = Y;
  bX = X;
  changeX = getRandomInt(-10, 10);
  changeY = getRandomInt(5,10);
  rectWidth = 150;
  stop = width - rectWidth;//makes paddle go to right side of screen
  circWidth = 20;
  direction = "up";
  points=0;
  end = false;
  noLoop();
  looper = 0;
  backgroundCol = (100);
  ballCol = (0);
  ballLine = (200);
  paddleCol = (0);
  paddleLine = (200);
  // gameover = loadImage("gameover.png")
}



// draw loop
void draw(){
  // Fill canvas
background(backgroundCol);
//points box

  fill(100)
  var pointsText ="points:"+points
  rect( 2, 2, textWidth(pointsText)+20, 40);
  fill(255)
  textFont("Ariel",34)
  text(pointsText,10,35);
  //draw paddle
  fill(paddleCol);
  stroke(paddleLine);
  rect( X, Y, rectWidth,20);
  //draw ball
  fill(ballCol);
  stroke(ballLine);
  ellipse(bX, bY, circWidth, circWidth);

  // keep from going off screen

  X+=(nX-X)/delay;
  if (X >= stop){
    X = stop
  }

 if (bY > 470) {
     end = true;
 };
//change directions when they hit the wall
  if (direction == "up") {
    bX += changeX;
    bY -= changeY;
  };

   if (bY <= 0) {
     changeX = getRandomInt(-10, 10);
     direction = "down";
  };

   if (direction == "down") {
      bX += changeX;
      bY += changeY;
    };
//change direction on paddle
  if ((bY >= Y-5) && (bY <= Y + 25)  &&  (bX>=X) && (bX <= (X+rectWidth)) ) {
    points++;
    changeX = getRandomInt(-10, 10);
    direction = "up";
  };
   if ((bX >= 700)  && (bY <= 450)){
     changeX = getRandomInt(-10, 10);
     direction = "left";
   };

   if (direction == "left") {
    bX -= changeY;
    bY += changeX;
   }
   if ((bX <= 0) && (bY <= 450)) {
     changeX = getRandomInt(-10, 10);
     direction = "right";
   }

   if (direction == "right") {
    bX += changeY;
    bY += changeX;
   }
   if(looper==0){
     //start screen
     mono = loadFont("Arial", 32);
     background(0);
     fill(0,155,0)
     textFont(mono);
     text(">> click screen to run code", 12, 60);
     looper++;//makes it only run once
   }
   //draw end screen
   if(end){
    background(102,255,153);
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var imageObj = new Image();
    imageObj.src = 'gameover.png';
    context.drawImage(imageObj, (width-400)/2, 100);
    var pointsText ="final points:"+points
    fill(100)
    rect((width-textWidth(pointsText)+20)/2-10,300, textWidth(pointsText)+20, 40);
    fill(255)
    textFont("Ariel",34)
    text(pointsText,(width-textWidth(pointsText)+20)/2,330);
    noLoop();
   }

};
//starts loop when canvas clicked
void mousePressed() {
  loop();

}
// if (keyPressed == true) {
//     // Restart the program whenever the user clicks the mouse
//     Program.restart();
// };

//
void setColor(r,g,b){
    backgroundCol = color(r,g,b);
}
void setBallColor(r,g,b){
    ballCol = color(r,g,b);
}
void setBallLine(r,g,b){
    ballLine = color(r,g,b);
}
void setPaddleColor(r,g,b){
    paddleCol = color(r,g,b);
}
void setPaddleLine(r,g,b){
    paddleLine = color(r,g,b);
}
void setRectWidth(num){
  rectWidth = num
}
void setCircWidth(num){
  circWidth = num
}
// track mouse
void mouseMoved(){
  nX = mouseX;
}
