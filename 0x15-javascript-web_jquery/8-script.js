$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (data) {
    data.results.forEach(function (ithem) {
      $('ul#list_movies').append('<li>' + ithem.title + '</li>');
    });
  }
});
