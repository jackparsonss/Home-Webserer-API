function getData(){
    var dataDocument = document.getElementById("data");
    fetch('/api/get-data')
    .then(response => response.json())
    .then(data => {
      time = Object.keys(data)
      var div = document.createElement("h3");
      div.innerHTML = 'Temperature: ' + data[time].Temperature + 'C <br/> Humidity ' + data[time].Humidity + "%";
      dataDocument.appendChild(div);
    });
  }