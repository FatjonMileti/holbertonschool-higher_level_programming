$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (query) {
    $('#character').text(query.name);
});