const form = document.querySelector('form');
const resultsDiv = document.querySelector('#results');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const message = form.querySelector('textarea').value;
  
  fetch('/check-spam', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message })
  })
  .then(response => response.json())
  .then(data => {
    if (data.isSpam) {
      resultsDiv.innerHTML = '<p>This message has been reported for spam.</p>';
    } else {
      resultsDiv.innerHTML = '<p>This message is not reported for spam.</p>';
    }
  })
  .catch(error => {
    console.error(error);
    resultsDiv.innerHTML = '<p>There was an error checking the message for spam. Please try again later.</p>';
  });
});
