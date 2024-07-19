document.querySelector('form').addEventListener('submit', function(event) {
    let valid = true;
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        if (!input.value) {
            valid = false;
            input.style.borderColor = 'red';
        } else {
            input.style.borderColor = '#ccc';
        }
    });
    if (!valid) {
        event.preventDefault();
        alert('Please fill in all fields.');
    }
});
