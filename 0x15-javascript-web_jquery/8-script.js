$(document).ready(function(){
  var link = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.getJSON( link, function( json ) {
    for (var i = 0; i < json.results.length; i++) {
      $("#list_movies").append('<li>'+ json.results[i].title + '</li>');
    }
  });
});
