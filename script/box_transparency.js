window.onload = function() {
  console.log( "Hello World" );
}


function box_fade( note )
{
  console.log("Box-fade: " + note );
  let div = document.getElementById( "0" );
  // div.setAttribute("class", "transparent_box");
  div.className += " transparent_box";

}
