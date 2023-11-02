// This script adds, removes and clears LI elements from a list upon clicking
$(document).ready(function() {
  $('#add_item').click(function() {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });

  $('#remove_item').click(function() {
    const list = $('ul.my_list');
    list.children().last().remove();
  });

  $('#clear_list').click(function() {
    const list = $('ul.my_list');
    list.empty();
  });
});
