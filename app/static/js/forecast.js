// $("#forecast").click(() => {
function myfunction() {
  var BUILD_YEAR = $("#BUILD_YEAR").val();
  var BEDROOMS = $("#BEDROOMS").val();
  var BATHROOMS = $("#BATHROOMS").val();
  var LAND_AREA = $("#LAND_AREA").val();
  var FLOOR_AREA = $("#FLOOR_AREA").val();
  var CBD_DIST = $("#CBD_DIST").val();
  var NEAREST_SCH_RANK = $("#NEAREST_SCH_RANK").val();
  console.log(BUILD_YEAR);
  console.log(BEDROOMS);
  console.log(BATHROOMS);
  console.log(LAND_AREA);
  console.log(FLOOR_AREA);
  console.log(CBD_DIST);
  console.log(NEAREST_SCH_RANK);
  $.getJSON(
    // $.pd.to_json(
    `/api/predict/${BUILD_YEAR}/${BEDROOMS}/${BATHROOMS}/${LAND_AREA}/${FLOOR_AREA}/${CBD_DIST}/${NEAREST_SCH_RANK}`,
    (predicted) => {
      var PRICE = Math.floor(predicted.prediction);
      $("#forecasted-price").html(`
        <p>${PRICE}</p>
        `);
    }
  );
  // });
}
