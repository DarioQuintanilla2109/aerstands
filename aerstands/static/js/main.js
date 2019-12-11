const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
