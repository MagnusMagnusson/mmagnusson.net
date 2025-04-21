window.addEventListener("load", (event) => {
    document.getElementById('language-change').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        const data = new URLSearchParams();
        data.append('language', window.language === 'is' ? 'en':'is');
        data.append('next', location.pathname);
    
        fetch('/i18n/setlang/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': window.csfr
            },
            body: data.toString()
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            console.log(response.text());
        })
        .then(result => {
            console.log(result);
        })
        .catch(error => {
            console.error('language change error:', error);
        });
    });
  });
