import requests
import json
import gradio as gr

# Ollama API endpoint
url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codeassistant",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = response.json()
        return data.get("response", "")
    else:
        return f"Error: {response.text}"

# Gradio Interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(
        lines=5,
        placeholder="Enter your prompt here...",
        label="Prompt"
    ),
    outputs=gr.Textbox(
        lines=18,
        label="Model Response",
        
    ),
    title="Code Assistant",
    description="Local LLM powered by Ollama",
)

interface.launch()
