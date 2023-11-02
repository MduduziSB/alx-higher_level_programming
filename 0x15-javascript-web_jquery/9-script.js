/*
 * This script fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
 * and displays the value of hello from that fetch in the HTML tag DIV#hello
 */
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'GET',
  success: function (data) {
    $('#hello').text(data.hello);
  }
});
