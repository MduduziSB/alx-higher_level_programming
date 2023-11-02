$(document).ready(function () {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const lang = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang;
    
    $.get(url, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Language not found');
    });
  }
});
