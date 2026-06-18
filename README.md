# 🤖 Personal AI Chatbot

A simple and elegant AI chatbot built using **Flask** and **Ollama**. This project allows users to interact with a locally running Large Language Model (LLM) through a clean web interface.

---

## 🌐Live preview
link

## 🚀 Features

- 💬 Interactive AI chatbot interface
- 🎨 Modern and responsive frontend using HTML & CSS
- ⚡ Powered by Ollama and Llama 3.2
- 📝 Displays user queries and AI responses in chat bubbles
- 📱 Mobile-friendly design
- 🔒 Runs completely on your local machine

---

## 🛠️ Tech Stack

- Python
- Flask
- Ollama
- HTML5
- CSS3

---

## 📂 Project Structure

```
Personal-AI-Chatbot/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── home.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/personal-ai-chatbot.git

cd personal-ai-chatbot
```

### 2. Create a virtual environment (Optional)

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download Ollama from:

https://ollama.com/download

After installation, pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

Make sure the Ollama server is running before starting the Flask application.

---

## ▶️ Run the project

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Preview

- Clean and modern chatbot interface
- User and AI messages displayed separately
- Professional styling with responsive layout

---

## ⚠️ Important Note

This project uses **Ollama running locally**.

If you deploy this project to services like **Render**, **Vercel**, or **Railway**, the chatbot will not work unless an Ollama server is also hosted and accessible.

---

## 🌟 Future Improvements

- Chat history
- Streaming responses
- Voice input
- Dark/Light mode
- File upload support
- Markdown rendering
- AI typing animation

---

## 👨‍💻 Author

**Harsha Paloju**

If you found this project helpful, consider giving it a ⭐ on GitHub!