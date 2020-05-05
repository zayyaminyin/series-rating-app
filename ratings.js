"use strict";

function getSeries(){
    ajaxGetRequest("series", displaySeries);
}

function displaySeries(response){
    let series = JSON.parse(response);
    let div_html = ""
    for (let series_id in series) {
      let serieS = series[series_id];
      div_html = div_html + generate_series_html(serieS);
    }
    let seriesDiv = document.getElementById("series");
    seriesDiv.innerHTML = div_html;
}

function newSeries() {
  let id_elem = document.getElementById("series_id_input");
  let series_id = get_value_and_clear(id_elem);
    
  let title_elem = document.getElementById("series_title_input");
  let title = get_value_and_clear(title_elem);
    
  let network_elem = document.getElementById("series_network_input")
  let network = get_value_and_clear(network_elem);
    
  let series = {"series_id": series_id, "title": title, "network": network};
  let seriesJSON = JSON.stringify(series);
  ajaxPostRequest("add_series", seriesJSON, displaySeries)
}

function rate(series_id, rating){
  let seriesRating = {"series_id": series_id, "rating": rating};
  let ratingJSON = JSON.stringify(seriesRating);
  ajaxPostRequest("rate_series", ratingJSON, displaySeries)
}
