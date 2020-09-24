$(function () {
    var count = 0;
    $('#toggle_header').click(function () {
    count ++;
    $('header').toggleClass( 'red', count % 2 === 0 );
    $('header').toggleClass('green', count % 2 === 1);
    });
  });