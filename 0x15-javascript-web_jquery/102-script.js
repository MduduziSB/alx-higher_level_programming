$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang;

    $.ajax({
      url: apiUrl,
      type: 'GET',
      success: function (data) {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});

