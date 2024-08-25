document.getElementById('crawlForm').onsubmit = function(e) {
    e.preventDefault();
    const base_url = e.target.base_url.value;
    const max_depth = e.target.max_depth.value;
    const max_pages = e.target.max_pages.value;

    fetch('/crawl', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({base_url, max_depth, max_pages})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('crawlResults').innerText = JSON.stringify(data.targets, null, 2);
    });
};

document.getElementById('sqlInjectionForm').onsubmit = function(e) {
    e.preventDefault();
    const url = e.target.url.value;

    fetch('/test_sql_injection', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({url})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('sqlInjectionResults').innerText = data.message;
    });
};
