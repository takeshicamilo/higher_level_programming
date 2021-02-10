$(document).ready(function(){
  var link = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.getJSON( link, function( json ) {
        $('#character').text(json.name);
   });
});
