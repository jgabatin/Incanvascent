window.onload = function() {
  let songChoice = document.querySelectorAll(".song");
  // console.log( songChoice );
  for( var i = 0; i < songChoice.length; i ++ )
  {
    // console.log( songChoice[i]);
    songChoice[i].onclick = onSongClick;
  }

}



function onSongClick(evt)
{
  song_key = evt.target.id;


  // console.log( song_key);
  sendData(song_key);
}

function sendData(data){
  // console.log( data );
  var xhr = new XMLHttpRequest();
  xhr.open("GET", '/piano_page', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  var actualObject = {'data': data}
  xhr.send(JSON.stringify(actualObject));
}
