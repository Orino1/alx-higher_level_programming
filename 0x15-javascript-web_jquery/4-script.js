$('div#red_header').click(function () {
  if ($('body header').hasClass('red')) {
    $('body header').removeClass('red');
    $('body header').addClass('green');
  } else {
    $('body header').removeClass('green');
    $('body header').addClass('red');
  }
});
