// frontend/app.js

// Using the Web Speech API
let recognition;

if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
} else if ('SpeechRecognition' in window) {
    recognition = new SpeechRecognition();
}

// Chat message handling
const chatInput = document.getElementById('chat-input');
const chatLog = document.getElementById('chat-log');

function addMessageToChatLog(message) {
    const messageElement = document.createElement('div');
    messageElement.innerText = message;
    chatLog.appendChild(messageElement);
}

// Function to handle speech recognition results
recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    chatInput.value = transcript;
    addMessageToChatLog(`You: ${transcript}`);
    sendMessageToBackend(transcript);
};

// Send messages to backend API endpoints
async function sendMessageToBackend(message) {
    try {
        const response = await fetch('https://your-backend-api-endpoint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message }),
        });
        const data = await response.json();
        addMessageToChatLog(`Bot: ${data.reply}`);
    } catch (error) {
        console.error('Error sending message to backend:', error);
    }
}

// Start recognition
recognition.start();

// HTML elements event listeners
chatInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        const message = chatInput.value;
        addMessageToChatLog(`You: ${message}`);
        sendMessageToBackend(message);
        chatInput.value = '';
    }
});
