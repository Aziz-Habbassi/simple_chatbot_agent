# Local Chatbot (Python + LangChain + Ollama)

A simple web-based chatbot that runs local LLMs via Ollama, featuring a clean Python UI and a modular LangChain pipeline for prompts and memory.

> **Important:** Before running the app, download a model with Ollama (e.g., `llama3.1:8b`). You can choose any supported model.

```bash
ollama pull llama3.1:8b
```

---

## Features

- Local, private inference via Ollama-managed models.  
- Web UI for chat with conversation memory.  
- Easily switch models and adjust generation settings.  
- Lightweight, hackable Python + LangChain stack.  

---

## Prerequisites

- Python 3.10+  
- Ollama installed and running: [https://ollama.com](https://ollama.com)  
- At least one model pulled, e.g.:  

```bash
ollama pull llama3.1:8b
```

> Tip: List installed models with:  

```bash
ollama list
```

---

## Quick Start

1. **Clone the repository**:

```bash
git clone https://github.com/Aziz-Habbassi/simple_chatbot_agent.git
cd "your-repo-folder"
```

3. **Pull a model (if not already done)**:

```bash
ollama pull llama3.1:8b
```

5. **Run the app** (choose your framework):

- **Streamlit**:

```bash
streamlit run simple_ai_chatbot.py
```

Open the UI in your browser (e.g., [http://localhost:8000](http://localhost:8000) or the URL printed by your framework).  

---


## Model Management

- **List installed models**:

```bash
ollama list
```

- **Pull a different model**:

```bash
ollama pull mistral
```

- **Remove a model**:

```bash
ollama rm <model_name>
```

---

## Project Structure

```
simple_ai_chatbot.py          — full app.
```

---

## Troubleshooting

- **Ollama not found**: Ensure Ollama is installed and running.  
- **Model not found**: Run `ollama pull <model>` and verify `MODEL_NAME` matches.  
- **CORS or port issues**: Confirm the app’s port is free and `OLLAMA_HOST` is reachable.

