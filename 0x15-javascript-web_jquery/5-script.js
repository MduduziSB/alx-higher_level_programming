/*
 * This script adds a <li> element to a list
 * when the user clicks on the tag DIV#add_item
 */
$(document).ready(function () {
  $('#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });
});
