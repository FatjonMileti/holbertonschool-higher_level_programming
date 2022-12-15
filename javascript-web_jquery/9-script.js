$.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', function (query) {
    $('#hello').text(query.hello);
});