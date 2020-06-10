// d3.json("/data").then(data => console.log(data))
(async function() {
  var data = await d3.json("/data")

  console.log(data);

  var plotData = [{
    x : data.map(row => row.name),
    y : data.map(row => row.age),
    type : "bar"
  }]

  var layout = {
    title : "Age"
  }

  Plotly.newPlot("plot", plotData, layout);
})();

d3.selectAll(".person").on("mouseover", function(){
  d3.select(this).style("color", "blue");
}).on("mouseout", function(){
    d3.select(this).style("color", "black");
}).on("click", function(){
})
