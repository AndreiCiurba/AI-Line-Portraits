//point arrays
let pointArrayX = [];
let pointArrayY = [];
let width = 800;
let height = 800;
let r = 300;
let items = 60;

let stringColor = "black";
let backgroundColor = "white";

let particles = [];

let randomLines = 1000;

//TODO add timeout function

function setup() {
  let canvas = createCanvas(width, height);
  getCircle(width/2, height/2,r, items);
  background(backgroundColor);
  strokeWeight(7);
  displayNails(pointArrayX, pointArrayY);
  // randomizePoints(x0,y0,r,items);
  strokeWeight(0.4);
  stroke(stringColor);
  drawRandomLines(pointArrayX,pointArrayY,randomLines);
}

function draw() {
  //display Nails

  //display Lines


  // randomNLines(pointArrayX,pointArrayX, items, nrLines);

}
