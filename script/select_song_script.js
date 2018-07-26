window.onload = function() {
  let songChoice = document.querySelectorAll("a");
  songChoice.onclick = onSongClick;
}



function onSongClick(evt)
{
  song_id = evt.target.id;
  sendData(song_id);
  console.log( song_id);

}

function sendData(data){
  var xhr = new XMLHttpRequest();
  xhr.open("GET", '/get_song', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  var actualObject = {'data': data}
  xhr.send(JSON.stringify(actualObject));
}
