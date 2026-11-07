# FastAPI + LangChain Vision AI Assistant

A high-performance multimodal AI assistant built with **FastAPI**, **LangChain**, **LangGraph**, and **Google Gemini 3.5 Flash**, accompanied by a minimalist web interface inspired by Linear and Claude.

---

## Features

- **Multimodal Visual Analysis:** Inspect, transcribe, analyze, and discuss images (PNG, JPEG, WebP, GIF) or ask pure text questions.
- **Multi-Session Memory Checkpoints:** Built-in conversation memory powered by LangGraph `InMemorySaver`. Each chat thread maintains an isolated memory context indexed by `thread_id`.
- **Dynamic Memory Management:** Dedicated endpoint to clear or reset memory for specific conversation threads.
- **Zero-Dependency Minimalist UI:** Modern, distraction-free web client featuring:
  - Drag-and-drop file staging & clipboard paste support (`⌘V` / `Ctrl+V`).
  - High-resolution image lightbox viewer.
  - Multi-chat sidebar with local history persistence.
  - Live backend health status check (Online/Offline indicator).
  - Text-to-speech (TTS) audio readback.
  - One-click copy and Markdown export.

---

## Architecture Overview

```
[ Frontend: Web Client ]
       │
       │  multipart/form-data (prompt + image + thread_id)
       ▼
[ FastAPI App: main.py ]
       │
       ▼
[ Router: /api/v1/chat ]
       │
       ▼
[ Service: analysis.py ]
       │  (Base64 serialization + dynamic MIME typing)
       ▼
[ LangGraph Agent: graph.py ] ◄──► [ InMemorySaver Checkpointer ]
       │                            (Thread state & memory)
       ▼
[ Google GenAI: Gemini 3.5 Flash ]
```

---

## Project Structure

```
.
├── agent/
│   └── graph.py           # LangGraph agent setup with memory checkpointer
├── api/
│   └── v1/
│       └── chat.py        # POST /chat and DELETE /chat endpoints
├── config.py              # Environment and model configurations
├── frontend/
│   ├── index.html         # Modern single-page web client (Zero build required)
│   └── README.md          # Frontend documentation
├── main.py                # FastAPI entry point & CORS configuration
├── model/
│   └── request.py         # Pydantic request models with multipart support
├── service/
│   └── analysis.py        # Multimodal payload construction & model invocation
├── .env.example           # Example environment variables template
├── .gitignore             # Git ignore configuration (secrets & cache protection)
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## Getting Started

### 1. Prerequisites
- **Python 3.11+**
- A **Google Gemini API Key** from [Google AI Studio](https://aistudio.google.com/)

### 2. Clone the Repository
```bash
git clone https://github.com/rahulrajesh21/fastapi-langchain-vision.git
cd fastapi-langchain-vision
```

### 3. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy the example environment file and insert your Gemini API key:
```bash
cp .env.example .env
```

Edit `.env`:
```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here
PORT=8000
ENVIRONMENT=development
MODEL_NAME=google_genai:gemini-3.5-flash-lite
```

---

## Running the Application

### Start the FastAPI Backend
```bash
source venv/bin/activate
uvicorn main:app --reload --port 8000
```
- Swagger UI Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Interactive API ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Launch the Frontend
Double-click `frontend/index.html` or open it directly in your browser:
```bash
open frontend/index.html
```

*(Alternatively, serve via Python: `python3 -m http.server 3000 --directory frontend`)*

---

## API Endpoints

### 1. Send Message / Analyze Image
* **URL:** `/api/v1/chat`
* **Method:** `POST`
* **Content-Type:** `multipart/form-data`
* **Parameters:**
  | Field | Type | Required | Description |
  |---|---|---|---|
  | `prompt` | `string` | Yes | Text question or instructions for the model |
  | `image` | `file` | No | Image binary file (PNG, JPEG, WebP, GIF) |
  | `thread_id` | `string` | No | Conversation thread identifier (defaults to `"default"`) |

* **Response:**
  ```json
  "This image displays an application icon combining the letter 'A' with musical elements..."
  ```

### 2. Clear Conversation Thread Memory
* **URL:** `/api/v1/chat`
* **Method:** `DELETE`
* **Query Parameters:**
  | Parameter | Type | Required | Description |
  |---|---|---|---|
  | `thread_id` | `string` | No | ID of the thread to clear (defaults to `"default"`) |

* **Response:**
  ```json
  {
    "message": "Chat history deleted successfully"
  }
  ```

---

## License
MIT License. Free for open source and commercial use.
