let bars = [];
let i,j;
let bars_width = 2; 
/* width of a single bar, value is inversly proportional to the number of bars/lines that will be seen on the screen*/
function setup() {
  createCanvas(600, 500);
  
  bars = new Array(width / bars_width);
  
  fill('white');
  for(i = 0; i < bars.length; i++)
    {
      bars[i] = random(height);
      //console.log(bars[i]);
    }
  console.log("Sorting the bars using Bubble ssort");
  i = 0;

}

function draw() {
  background(0);
  if(i > bars.length) 
    {
      console.log("Done Sorting");
      noLoop();
    } else {
        for(let j = 0; j < bars.length - 1- i; j++)
      {
        let a = bars[j];
        let b = bars[j + 1];
        if(a > b)
          {
            swap(bars, j, j + 1)
          }
      }
    }
    i++;
  
  stroke('white');
  fill('white');
  for(let i = 0; i < bars.length; i++)
    {
      rect(i * bars_width, height - bars[i], bars_width - 2, bars[i]);
    }
}

function swap(arr, a, b) {
  let temp = arr[a];
  arr[a] = arr[b];
  arr[b] = temp;
}
