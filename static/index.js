function getData(){
    fetch('/get-data')
    .then(response => response.json())
    .then(data => console.log(data));
}