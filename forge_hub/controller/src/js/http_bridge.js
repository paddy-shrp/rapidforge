INTERNAL_URL = "https://admin.example.com/internal/"

function sendGETRequest(url) {
    return fetch(url, {
        method: "GET"
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(response.statusText);
        }
        return response.json()
    })
    .catch(error => console.error('Error:', error));
}

function sendRequest(url, method="GET", data={}) {
    if(method == "GET") return sendGETRequest(url)
    return fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(response.statusText);
            }
            return response.json()
        })
        .catch(error => console.error('Error:', error));
}

function sendInternalRequest(url, method="GET", data={}) {
    return sendRequest(INTERNAL_URL + url, method, data)
}

function sendServerOperation(prefix, op) {
    message = "Perform: " + prefix + " " + op
    if(confirm(message)) {
        return sendRequest(INTERNAL_URL + "operations/" + prefix + "/" + op, "PUT")
    }
}