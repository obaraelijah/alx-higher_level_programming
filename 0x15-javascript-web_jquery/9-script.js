const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(url, (body) => {
    $('#hello').text(body.hello);
});