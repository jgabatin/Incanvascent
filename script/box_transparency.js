var note_progression;
var counter;


window.onload = function() {
  console.log( "Hello World" );

  var img = document.getElementById("art");
  img.style.visibility = 'hidden';
  call_back();

}



function call_back()
{
  //Reset Global Variables
  note_progression = Song.note_progression;
  counter = 0;

  var notes_location = document.getElementById("song_notes");
  for( var i = 0; i < note_progression.length; i ++ )
  {
    notes_location.innerText += " " + note_progression[i];
  }



  var img = document.getElementById("art");
  img.style.visibility = 'visible';

  dimension = Song.type;
  html = document.getElementById( "hid" );
  html.style.gridTemplateColumns = "repeat(" + dimension + ", " + (100/dimension) + "%)";
  html.style.gridTemplateRows = "repeat(" + dimension + ", " + (100/dimension) + "%)";
  for( var r = 0; r < dimension; r ++ )
  {
    for( var c = 0; c < dimension; c ++ )
    {
      var newElem = html.appendChild( document.createElement('div') )
      // newElem.style.height = "100%"; //+ (100/dimension) + "%";
      // newElem.style.width = "100%"; //+ (100/dimension) + "%";
      newElem.id = (r * dimension + c);
      newElem.className = "opaque_box";
    }
  }
}





function box_fade( note )
{
  if( note == note_progression[counter] )
  {
    var div, arr;
    div = document.getElementById("" + counter);
    arr = div.className.split(" ");
    if (arr.indexOf("transparent_box") == -1) {
        div.className = "transparent_box";
    }
    counter ++;
    console.log( counter );

    if( counter == note_progression.length )
    {
      for( var i = note_progression.length; i < Math.pow( Song.type, 2 ); i ++ )
      {
        console.log( i );
        div = document.getElementById("" + i);
        console.log( div );
        arr = div.className.split(" ");
        if (arr.indexOf("transparent_box") == -1) {
            div.className = "transparent_box";
        }
      }
    }
  }




}
