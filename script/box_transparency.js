window.onload = function() {
  console.log( "Hello World" );


  var response = jQuery.get("/get_song");
  console.log( response )

  // for( var i = 0; i < 16; i ++ )
  // {
  //   div = document.getElementById("" + i);
  //   arr = div.className.split(" ");
  //   if (arr.indexOf("transparent_box") == -1) {
  //       div.className = "opaque_box";
  //   }
  // }

}




var counter = 0;

function box_fade( note )
{
  if( counter < 16 )
  {
    console.log("Box-fade: " + note );
    var div, arr;
    div = document.getElementById("" + counter);
    arr = div.className.split(" ");
    if (arr.indexOf("transparent_box") == -1) {
        div.className = "transparent_box";
    }

    counter ++;
  }


}
