function generate_series_html(series) {
  let retVal = "<a href=\"https://www.netflix.com/title/" + series.series_id + "\" target=\"_blank\">"
  retVal = retVal + series.title + " - " + series.network + "</a><br>";
  retVal = retVal + series.ratings + "<br>";
  retVal = retVal + "Rate: ";
  retVal = retVal + generate_rating_buttons(series.series_id);
  retVal = retVal + "<hr>";
  return retVal
}

function generate_rating_buttons(series_id) {
  let retVal = "";
  let array = [1, 2, 3, 4, 5];
  for(let i of array) {
    retVal = retVal + generate_button_html(series_id, i);
  }
  return retVal;
}

function generate_button_html(series_id, num) {
  let retVal = "<button onClick=\"rate(\'" + series_id + "\', " + num + ")\">";
  retVal = retVal +num+"</button>";
  return retVal;
}

function get_value_and_clear(input_obj) {
  let retVal = input_obj.value;
  input_obj.value = "";
  return retVal;
}