# 🧠 Code Assistant (Local LLM with Ollama)

A simple AI-powered **Code Assistant** built using **Python, Gradio, and Ollama** that runs completely **locally on your machine**.

This project provides a clean **web interface for interacting with a local LLM** to generate code, explanations, and programming help without relying on external APIs.

---

# 🚀 Features

- 🖥️ Runs a **local LLM using Ollama**
- 🎯 Interactive **Gradio UI**
- 💬 Maintains **conversation history**
- ⚡ Fast local responses
- 🔒 No external API calls (runs fully locally)

---

# 🏗️ Tech Stack

- **Python**
- **Gradio** – Web UI
- **Ollama** – Local LLM runtime
- **Requests** – API communication

---

# 💻 How It Works

1. The user enters a prompt in the **Gradio UI**.
2. The prompt is sent to the **Ollama API endpoint**:

```
http://localhost:11434/api/generate
```

3. The selected **local LLM model** generates a response.
4. The response is displayed in the Gradio interface.

The app also **stores conversation history** to maintain context.

---

# 🧩 Example Use Cases

- Generate code snippets
- Explain programming concepts
- Debug code
- Ask development questions
- Use as a lightweight **local coding copilot**

---

# 🔮 Future Improvements

- Streaming responses
- Chat-style UI
- Code syntax highlighting
- Multi-model support
- RAG support with documentation
- Docker deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Submit a pull request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Saketh Yedugani**

MS in Computer Science  
AI / LLM Engineer
