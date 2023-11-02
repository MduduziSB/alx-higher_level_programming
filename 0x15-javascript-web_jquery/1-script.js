// This script updates the text color of the <header> element to red (#FF0000)
const headerElements = document.getElementsByTagName('header');

if (headerElements.length > 0) {
  // Set the text color of the first found header element to red
  headerElements[0].style.color = '#FF0000';
}
