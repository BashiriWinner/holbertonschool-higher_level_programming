const redHeaderDiv = document.getElementById('red_header');
const header = document.querySelector('header');

redHeaderDiv.addEventListener('click', () => {
  header.classList.add('red');
});
