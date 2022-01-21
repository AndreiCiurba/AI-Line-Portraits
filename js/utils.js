function getCircle(x0,y0,r,nrPoints)
{
  for(var i = 0; i < nrPoints; i++) {
      var x = x0 + r * cos(2 * PI * i/ nrPoints);
      var y = y0 + r * sin(2 * PI * i / nrPoints);
      append(pointArrayX,x);
      append(pointArrayY,y);
    }
}
function displayNails(arrayX,arrayY)
{
  for(var i = 0; i < arrayX.length; i++){
    stroke('red');
    point(arrayX[i],arrayY[i]);
  }
}

function drawRandomLines(pointArrayX,pointArrayY,randomLines){
  let nrPoints = pointArrayX.length;
  let rand1 = Math.floor(Math.random()*(items));
  let rand2;


  for (var i = 0; i < randomLines; i++)
  {
    rand2 = Math.floor(Math.random()*(items));
    line(pointArrayX[rand1],pointArrayY[rand1],
      pointArrayX[rand2],pointArrayY[rand2]);
    rand1 = rand2;
  }

}

// 
// function keyTyped() {
//   if (key === 's') {
//     saveCanvas('myCanvas', 'png');
//   }
// }
