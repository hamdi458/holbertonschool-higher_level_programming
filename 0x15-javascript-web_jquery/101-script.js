$(function () {
    $('#add_item').click(function () {
      $('ul').append('<li>Item</li>');
    });
    $('#remove_item').click(function () {
      $('ul li:last').remove();
    });
    $('#clear_list').click(function () {
      $('ul').empty();
    });
  });