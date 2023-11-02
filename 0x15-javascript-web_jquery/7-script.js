$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: function (data) {
    $('div#character').text(data);
  }
});
