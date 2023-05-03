const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$(document).ready(() => {
    $.get(url, function (data) {
    $.each(data.results, function (i, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});
});