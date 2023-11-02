function fetchit () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=' + $('INPUT#language_code').val(),
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
}
$(function () {
  $('INPUT#btn_translate').click(fetchit);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchit();
    }
  });
});
