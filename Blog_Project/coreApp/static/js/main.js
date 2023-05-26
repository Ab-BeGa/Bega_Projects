const form = document.querySelector('form');
const input = document.querySelector('#search-box');
const results = document.querySelector('#search-results');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const query = input.value;
  const response = await fetch(`/search?q=${query}`);
  const data = await response.json();

  results.innerHTML = '';

  data.forEach((item) => {
    const li = document.createElement('li');
    li.textContent = item.title;
    results.appendChild(li);
  });
});
