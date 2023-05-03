const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$(document).ready(() => {
    $.getJSON(url, (data) => {
        $('#character').text(data.name)
    });
});