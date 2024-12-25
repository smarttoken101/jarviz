document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const voiceBtn = document.getElementById('voice-btn');

    function addMessage(message, isUser = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = isUser ? 'user-message' : 'ai-message';
        messageDiv.innerHTML = `<p>${message}</p>`;
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    function showTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.className = 'typing-indicator';
        indicator.innerHTML = '<span></span><span></span><span></span>';
        chatContainer.appendChild(indicator);
        chatContainer.scrollTop = chatContainer.scrollHeight;
        return indicator;
    }

    async function processUserInput(message) {
        addMessage(message, true);
        const indicator = showTypingIndicator();

        try {
            const response = await fetch('/process_text', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            indicator.remove();
            addMessage(data.response);
        } catch (error) {
            indicator.remove();
            addMessage('Sorry, I encountered an error. Please try again.');
            console.error('Error:', error);
        }
    }

    async function processVoiceInput() {
        voiceBtn.disabled = true;
        voiceBtn.style.backgroundColor = '#718096';
        
        try {
            const response = await fetch('/process_voice', {
                method: 'POST'
            });
            
            const data = await response.json();
            addMessage(data.response);
        } catch (error) {
            addMessage('Sorry, I encountered an error with voice processing. Please try again.');
            console.error('Error:', error);
        } finally {
            voiceBtn.disabled = false;
            voiceBtn.style.backgroundColor = '';
        }
    }

    sendBtn.addEventListener('click', () => {
        const message = userInput.value.trim();
        if (message) {
            processUserInput(message);
            userInput.value = '';
        }
    });

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            const message = userInput.value.trim();
            if (message) {
                processUserInput(message);
                userInput.value = '';
            }
        }
    });

    voiceBtn.addEventListener('click', processVoiceInput);
});
