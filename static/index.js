function getData(){
    fetch('/api/get-data')
    .then(response => response.json())
    .then(data => console.log(data));
}