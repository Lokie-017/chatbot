function sendMessage() {
    let userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><b>You:</b> ${userInput}</p>`;

    fetch('/get-response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById('user-input').value = '';
}
