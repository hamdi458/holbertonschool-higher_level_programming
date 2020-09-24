$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?lang='  ;

    $('INPUT#btn_translate').click(function () {

      const api = url + $('#language_code').val();
      $.get( api , function (data) {
        $('DIV#hello').html(data.hello);
      });
    });
  });