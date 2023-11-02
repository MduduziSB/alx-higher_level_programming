/*
 * This script fetches the character name from the following URL:
 * https://swapi-api.alx-tools.com/api/people/5/?format=json
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  type: 'GET',
  success: function (data) {
    const characterName = data.name;
    $('DIV#character').text(characterName);
  }
});
