$(document).ready(function(){
  $("#toggle_header").click(function(){
    if ($(".red")[0]) {

      $(this).toggleClass('green');
    }
    else {
      $(this).toggleClass('red');
    }
  });
});
