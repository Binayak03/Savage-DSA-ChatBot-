document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    sendBtn.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value;
        if (message.trim() === "") return;

        addMessage("user", message);
        userInput.value = "";

        fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message }),
        })
            .then((response) => response.json())
            .then((data) => {
                addMessage("bot", data.reply);
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    function addMessage(sender, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("chat-message", `${sender}-message`);
        messageElement.innerText = message;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});