/* This script updates the text color of the <header> element to red (#FF0000)
 * when the user clicks on the tag DIV#red_header
 */
$(document).ready(function () {
  $('DIV#red_header').click(function () {
    // Update the text color of the header element to red (#FF0000)
    $('header').css('color', '#FF0000');
  });
});
