// static/script.js
const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');

// Function to add a message to the chatbox
function addMessage(message, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
    // Basic sanitization to prevent HTML injection (more robust sanitization needed for production)
    messageDiv.textContent = message;
    chatbox.appendChild(messageDiv);
    // Scroll to the bottom
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Function to handle sending a message
async function sendMessage() {
    const query = userInput.value.trim();
    if (!query) return; // Don't send empty messages

    addMessage(query, 'user'); // Display user message
    userInput.value = ''; // Clear input field
    userInput.disabled = true; // Disable input while waiting
    sendButton.disabled = true; // Disable button while waiting

    // Optional: Add a loading indicator
    const loadingDiv = document.createElement('div');
    loadingDiv.classList.add('message', 'bot-message', 'loading-message');
    loadingDiv.textContent = 'Thinking...';
    chatbox.appendChild(loadingDiv);
    chatbox.scrollTop = chatbox.scrollHeight;

    try {
        // Send query to the backend API
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query }),
        });

        chatbox.removeChild(loadingDiv); // Remove loading indicator

        if (!response.ok) {
            // Handle HTTP errors (e.g., 500 internal server error)
            const errorData = await response.json().catch(() => ({ detail: 'Unknown server error' }));
            console.error('API Error:', response.status, errorData);
            addMessage(`Sorry, an error occurred: ${errorData.detail || 'Server error'}`, 'bot');
        } else {
            const data = await response.json();
            addMessage(data.answer, 'bot'); // Display bot response
        }
    } catch (error) {
        chatbox.removeChild(loadingDiv); // Remove loading indicator on fetch error
        console.error('Fetch Error:', error);
        addMessage('Sorry, I could not connect to the chatbot service.', 'bot');
    } finally {
         userInput.disabled = false; // Re-enable input
         sendButton.disabled = false; // Re-enable button
         userInput.focus(); // Put cursor back in input
    }
}

// Event listeners
sendButton.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', function(event) {
    // Send message if Enter key is pressed
    if (event.key === 'Enter') {
        sendMessage();
    }
});