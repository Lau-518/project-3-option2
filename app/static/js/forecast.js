// $("#forecast").click(() => {
d3.select("#forecast").on("click", () => {
  // function myfunction() {
  var BUILD_YEAR = d3.select("#BUILD_YEAR").node().value;
  var BEDROOMS = d3.select("#BEDROOMS").node().value;
  var BATHROOMS = d3.select("#BATHROOMS").node().value;
  var LAND_AREA = d3.select("#LAND_AREA").node().value;
  var FLOOR_AREA = d3.select("#FLOOR_AREA").node().value;
  var CBD_DIST = d3.select("#CBD_DIST").node().value;
  var NEAREST_SCH_RANK = d3.select("#NEAREST_SCH_RANK").node().value;

  console.log(BUILD_YEAR);
  console.log(BEDROOMS);
  console.log(BATHROOMS);
  console.log(LAND_AREA);
  console.log(FLOOR_AREA);
  console.log(CBD_DIST);
  console.log(NEAREST_SCH_RANK);
  d3.json(
    `/api/predict/${BUILD_YEAR}/${BEDROOMS}/${BATHROOMS}/${LAND_AREA}/${FLOOR_AREA}/${CBD_DIST}/${NEAREST_SCH_RANK}`
  ).then((predicted) => {
    var PRICE = Math.round(predicted.prediction * 100) / 100;
    d3.select("#forecasted-price").html(`
        <p>${PRICE}</p>
        `);
  });
});
// }
