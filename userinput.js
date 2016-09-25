function restartMe(){
  location.reload();
};
function setColor(r,g,b) {
  var pjs = Processing.getInstanceById("canvas");
  pjs.setColor(r,g,b);
  };
function setBallColor(r,g,b) {
  var pjs = Processing.getInstanceById("canvas");
  pjs.setBallColor(r,g,b);
    };
function setBallLine(r,g,b) {
  var pjs = Processing.getInstanceById("canvas");
  pjs.setBallLine(r,g,b);
  console.log(r,g,b)
        };
function setPaddleLine(r,g,b) {
  var pjs = Processing.getInstanceById("canvas")
  pjs.setPaddleLine(r,g,b)
};
function setPaddleColor(r,g,b){
  var pjs = Processing.getInstanceById("canvas")
  pjs.setPaddleColor(r,g,b)
}


//changes paddle
function setRectWidth(num){
  var pjs = Processing.getInstanceById("canvas")
  pjs.setRectWidth(num)
}




function setCircWidth(num){
  var pjs = Processing.getInstanceById("canvas")
  pjs.setCircWidth(num)
}
function handleChange() {
url = document.getElementById('stuff').value;
console.log(url);
}
function showCanvas(){
    var myCanvas = document.getElementById('canvas-container');
    myCanvas.style.display = 'block';
  };
  var clicked=0;
  function next_line() {
     clicked++;
     if (clicked == 1) {
       var sentenceone = document.getElementById('sentence_one');
       sentenceone.style.display = 'block';
       document.getElementById('explanation_box').innerHTML = "This section is for setting up. It runs just once at the beginning and sets the size and colors and speed of the objects. It's like packing your bag with all of the things that you need later. \n A function is an action that is made up of a lot of individual steps. Everyday in our own lives we complete functions. For instance, if someone tells you to set the table, they don't have to explain that it means that you have to set out the forks, knives, spoons, plates, and napkins because you know from past experience that that is what setting the table means. When we define functions, we are giving them that knowledge that when we call that function setTheTable(), it means that it has to complete all the little actions that we do instinctively.";
       document.getElementById('explanation_box').style.border = "3px solid #73AD21";
       document.getElementById('btn').innerHTML = "Next line";
    };
    if (clicked == 2) {
      var sentencetwo = document.getElementById('sentence_two');
      sentencetwo.style.display = 'block';
      document.getElementById('explanation_box').innerHTML = "Here you need to set up the color and size of the ball. After outline, put the color that you want the outline of the ball to be. After fill, put the color you want the ball itself to be. After size, put a number between ten and fifty that will establish the size of the ball. This number sets the number of pixels wide the ball will be. Pixels are tiny dots that make up the pictures on the screen.";
    };
    if (clicked == 3) {
      x = false
      ball_outline = document.getElementById('ball_outline').value;
      if (ball_outline.toUpperCase()=="GREEN"){
        setBallLine(0,255,0)
      }
      else if (ball_outline.toUpperCase()=="RED"){
        setBallLine(255,0,0)
      }
      else if (ball_outline.toUpperCase()=="BLUE"){
        setBallLine(0,0,255)
      }
      else if (ball_outline.toUpperCase()=="ORANGE"){
        setBallLine(255, 153, 0)
      }
      else if (ball_outline.toUpperCase()=="YELLOW"){
        setBallLine(255, 255, 102)
      }
      else if (ball_outline.toUpperCase()=="PURPLE"){
        setBallLine(179, 0, 134)
      }
      else if (ball_outline.toUpperCase()=="WHITE"){
        setBallLine(255,255,255)
      }
      else if (ball_outline.toUpperCase()=="BLACK"){
        setBallLine(0,0,0)
      }
      else if (ball_outline.toUpperCase()=="GRAY"){
        setBallLine(100,100,100)
      }
      else if (ball_outline.toUpperCase()=="PINK"){
        setBallLine(255, 77, 148)
      }
      else {
        console.log(ball_outline)
        alert("invalid outline color! try again")
        clicked = 2
        x = true
      }
      ball_color = document.getElementById('ballcolor').value;
      if (ball_color.toUpperCase()=="GREEN"){
        setBallColor(0,255,0)
      }
      else if (ball_color.toUpperCase()=="RED"){
        setBallColor(255,0,0)
      }
      else if (ball_color.toUpperCase()=="BLUE"){
        setBallColor(0,0,255)
      }
      else if (ball_color.toUpperCase()=="ORANGE"){
        setBallColor(255, 153, 0)
      }
      else if (ball_color.toUpperCase()=="YELLOW"){
        setBallColor(255, 255, 102)
      }
      else if (ball_color.toUpperCase()=="PURPLE"){
        setBallColor(179, 0, 134)
      }
      else if (ball_color.toUpperCase()=="WHITE"){
        setBallColor(255,255,255)
      }
      else if (ball_color.toUpperCase()=="BLACK"){
        setBallColor(0,0,0)
      }
      else if (ball_color.toUpperCase()=="GRAY"){
        setBallColor(100,100,100)
      }
      else if (ball_color.toUpperCase()=="PINK"){
        setBallColor(255, 77, 148)
      }
      else {
        alert("invalid ball color! try again")
        clicked=2
        x = true
       }
      if (x) {
        clicked = 2
      }
      else {
        var sentencethree = document.getElementById('sentence_three');
        sentencethree.style.display = 'block';
        document.getElementById('explanation_box').innerHTML = "Here you need to set up the color and size of the paddle. After outline, put the color that you want the outline of the paddle to be. After fill, put the color you want the paddle itself to be. The colors will be converted into three numbers that tell the computer which colors to combine to make the exact color that you want.";
      }
      ball_size = document.getElementById('ballsize').value;
      setCircWidth(ball_size)

   };
   if (clicked == 4) {
     y = false
     paddle_outline = document.getElementById('paddle_outline').value;
     if (paddle_outline.toUpperCase()=="GREEN"){
       setPaddleLine(0,255,0)
     }
     else if (paddle_outline.toUpperCase()=="RED"){
       setPaddleLine(255,0,0)
     }
     else if (paddle_outline.toUpperCase()=="BLUE"){
       setPaddleLine(0,0,255)
     }
     else if (paddle_outline.toUpperCase()=="ORANGE"){
       setPaddleLine(255, 153, 0)
     }
     else if (paddle_outline.toUpperCase()=="YELLOW"){
       setPaddleLine(255, 255, 102)
     }
     else if (paddle_outline.toUpperCase()=="PURPLE"){
       setPaddleLine(179, 0, 134)
     }
     else if (paddle_outline.toUpperCase()=="WHITE"){
       setPaddleLine(255,255,255)
     }
     else if (paddle_outline.toUpperCase()=="BLACK"){
       setPaddleLine(0,0,0)
     }
     else if (paddle_outline.toUpperCase()=="GRAY"){
       setPaddleLine(100,100,100)
     }
     else if (paddle_outline.toUpperCase()=="PINK"){
       setPaddleLine(255, 77, 148)
     }
     else {
       alert("invalid color! try again")
       y = true
     }
     paddle_color = document.getElementById('paddlecolor').value;
     if (paddle_color.toUpperCase()=="GREEN"){
       setPaddleColor(0,255,0)
     }
     else if (paddle_color.toUpperCase()=="RED"){
       setPaddleColor(255,0,0)
     }
     else if (paddle_color.toUpperCase()=="BLUE"){
       setPaddleColor(0,0,255)
     }
     else if (paddle_color.toUpperCase()=="ORANGE"){
       setPaddleColor(255, 153, 0)
     }
     else if (paddle_color.toUpperCase()=="YELLOW"){
       setPaddleColor(255, 255, 102)
     }
     else if (paddle_color.toUpperCase()=="PURPLE"){
       setPaddleColor(179, 0, 134)
     }
     else if (paddle_color.toUpperCase()=="WHITE"){
       setPaddleColor(255,255,255)
     }
     else if (paddle_color.toUpperCase()=="BLACK"){
       setPaddleColor(0,0,0)
     }
     else if (paddle_color.toUpperCase()=="GRAY"){
       setPaddleColor(100,100,100)
     }
     else if (paddle_color.toUpperCase()=="PINK"){
       setPaddleColor(255, 77, 148)
     }
     else {
       alert("invalid color! try again")
       y = true
      }


      //changes the paddle (calls function above)
    //  paddle_size = document.getElementById('paddlesize').value;
    //  setRectWidth(paddle_size)



     if (y) {
       clicked = 3
     }
     else {
       var sentencefour = document.getElementById('sentence_four');
       sentencefour.style.display = 'block';
       document.getElementById('explanation_box').innerHTML = "This makes sure that each time you play the game, you start with zero points.";
     }

   };
   if (clicked == 5) {
     var sentencefive = document.getElementById('sentence_five');
     sentencefive.style.display = 'block';
     document.getElementById('explanation_box').innerHTML = "This is a loop. It is like the setup function, but it runs over and over again. You can compare it to something that you do automatically without thinking over and over again every day, like breathing.";
   };
   if (clicked == 6) {
     z = false
     var sentencesix = document.getElementById('sentence_six');
     sentencesix.style.display = 'block';
     document.getElementById('explanation_box').innerHTML = "In this put the color you would like the backgroud to be.";
   };
   //data === parseInt(data, 10)
   if (clicked == 7) {
     z = false
     background = document.getElementById('background').value;
     if (background.toUpperCase()=="GREEN"){
       setColor(0,255,0)
     }
     else if (background.toUpperCase()=="RED"){
       setColor(255,0,0)
     }
     else if (background.toUpperCase()=="BLUE"){
       setColor(0,0,255)
     }
     else if (background.toUpperCase()=="ORANGE"){
       setColor(255, 153, 0)
     }
     else if (background.toUpperCase()=="YELLOW"){
       setColor(255, 255, 102)
     }
     else if (background.toUpperCase()=="PURPLE"){
       setColor(179, 0, 134)
     }
     else if (background.toUpperCase()=="WHITE"){
       setColor(255,255,255)
     }
     else if (background.toUpperCase()=="BLACK"){
       setColor(0,0,0)
     }
     else if (background.toUpperCase()=="GRAY"){
       setColor(100,100,100)
     }
     else if (background.toUpperCase()=="PINK"){
       setColor(255, 77, 148)
     }
     else {
       alert("invalid color! try again")
       z = true
      }
    if (z) {
      clicked = 6
    }
    else {
      var sentenceseven = document.getElementById('sentence_seven');
      sentenceseven.style.display = 'block';
      document.getElementById('explanation_box').innerHTML = "This allows the paddle to horizontally move where your mouse goes.";
    }
   };
   if (clicked == 8) {
     var sentenceeight = document.getElementById('sentence_eight');
     sentenceeight.style.display = 'block';
     document.getElementById('explanation_box').innerHTML = "This updates the ball and paddle with the changes that happened in the previous two steps.";
  };
  if (clicked == 9) {
    var sentencenine = document.getElementById('sentence_nine');
    sentencenine.style.display = 'block';
    document.getElementById('explanation_box').innerHTML = "This keeps the ball moving all the time.";
  };
  if (clicked == 10) {
    var sentenceten = document.getElementById('sentence_ten');
    sentenceten.style.display = 'block';
    document.getElementById('explanation_box').innerHTML = "These are conditionals that allow the ball to change its direction when certain things happen. This establishes that the ball will move in a straight line unless it touches the wall or the paddle.";
  };
  if (clicked == 11) {
    var sentenceeleven = document.getElementById('sentence_eleven');
    sentenceeleven.style.display = 'block';
    document.getElementById('explanation_box').innerHTML = "This is another conditional that sets up when the game is going to end.";
    document.getElementById('btn').innerHTML = "Run your code";
  };
  if (clicked == 12){
    showCanvas()
    window.scrollTo(0, 0);
    document.getElementById("refresh").style.display = "block";
  }
  }
