$(document).ready(function(){
  var link = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON( link, function( json ) {
        $('#hello').text(json.hello);
   });
});
