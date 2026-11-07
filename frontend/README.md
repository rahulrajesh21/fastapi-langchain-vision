# Vision AI Assistant - Frontend

A modern, minimalist web interface inspired by Linear and Claude for the FastAPI + LangChain Vision AI backend.

## Features
- **Multi-Session Memory:** Separate conversation threads, each tracked with its own `thread_id`.
- **Multimodal Chat:** Send text prompts with or without attached images.
- **Multiple Upload Methods:**
  - File picker (Paperclip icon)
  - Drag-and-drop images anywhere on the screen
  - **Paste from Clipboard (`Cmd+V` / `Ctrl+V`):** Paste screenshots directly into the chat!
- **Image Lightbox:** Click on any thumbnail to view it in full resolution with metadata.
- **Live Server Status:** Dynamic ping indicator in the header showing whether the FastAPI server is Online or Offline.
- **Thread Memory Reset:** Delete or reset thread memories on the server via `DELETE /api/v1/chat?thread_id=...`.
- **Text-to-Speech (TTS):** Audio readback for Gemini's answers.
- **Markdown & Code Rendering:** Formatted AI responses with syntax highlighting, lists, and tables.
- **Copy Response & Export:** One-click copy for answers, plus export entire conversations as `.md`.
- **Zero Dependencies:** Pure HTML5, Tailwind CSS, and Vanilla JavaScript. No `npm install` or build steps required.

---

## How to Run

### Step 1: Start your FastAPI backend
In your terminal, run:
```bash
source venv/bin/activate
uvicorn main:app --reload --port 8000
```

### Step 2: Open the Frontend
Choose whichever method you prefer:

#### Option A: Direct Open (macOS)
Double-click `frontend/index.html` or run:
```bash
open frontend/index.html
```

#### Option B: Simple Python Server
```bash
python3 -m http.server 3000 --directory frontend
```
Then visit `http://localhost:3000` in your browser.

#### Option C: Node / npx
```bash
npx serve frontend
```
