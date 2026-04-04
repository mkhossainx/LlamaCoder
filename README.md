# LlamaCoder API

A lightweight, serverless AI API built with Flask and deployed on Vercel. Powered by [Together AI](https://together.ai)'s LlamaCode backend — supports text prompts, optional image input, and multiple model tiers.

---

## About LlamaCoder

**LlamaCoder** is an expert frontend React engineer and UI/UX designer created by [Together AI](https://together.ai). It specializes in building beautiful, functional React applications using **TypeScript** and **Tailwind CSS** — making it ideal for generating UI components, full pages, and complete React apps from a simple text prompt.

---

## Features

- **Two model tiers** — `fast` for quick responses, `pro` for heavy workloads
- **Vision support** — pass an image URL alongside your prompt
- **Clean JSON responses** — simple, consistent output format
- **Zero-config deployment** — one-click deploy to Vercel
- **No API key required** — uses Together AI's public inference backend

---

## Endpoint

```
GET /api/ai
```

### Query Parameters

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `prompt`  | string | ✅ Yes   | The text prompt to send to the model |
| `model`   | string | ❌ No    | `fast` (default), `pro`, or `thinking` |
| `image`   | string | ❌ No    | Public image URL for vision input |

---

### Models

- **fast** → quick responses, low cost  
- **pro** → balanced performance  
- **thinking** → deeper reasoning, slower but more accurate (best for coding & complex tasks)

### Quality Modes

| Quality | Speed  | Description                                      |
|---------|--------|--------------------------------------------------|
| `low`   | ⚡ Fast  | Quicker responses, ideal for simple tasks        |
| `high`  | 🐢 Slower | More thorough output, better for complex prompts |

### Model Reference

| Alias       | Model                                        |
|------------|----------------------------------------------|
| `fast`     | `zai-org/GLM-4.6`                            |
| `pro`      | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`   |
| `thinking` | `deepseek-ai/DeepSeek-R1`                   |
---

## Usage Examples

**Basic prompt:**
```
GET /api/ai?prompt=Explain recursion in simple terms
```

**Using the pro model:**
```
GET /api/ai?prompt=Write a binary search in Python&model=pro
```
**Using the Thinking model:**
```
GET /api/ai?prompt=Write a binary search in Python&model=thinking 
```

**With an image:**
```
GET /api/ai?prompt=What is in this image?&image=https://example.com/photo.jpg
```

---

## Response Format

```json
{
  "status": true,
  "model": "fast",
  "response": "Recursion is when a function calls itself..."
}
```

**On error:**
```json
{
  "status": false,
  "error": "prompt required"
}
```

---

## Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)

**Steps:**

1. Fork or clone this repository
2. Go to [vercel.com/new](https://vercel.com/new) and import the repo
3. No environment variables needed — deploy as-is
4. Your API will be live at `https://your-project.vercel.app/api/ai`

---

## Local Setup

```bash
# Clone the repo
git clone https://github.com/mkhossainx/LlamaCoder
cd LlamaCoder

# Install dependencies
pip install -r requirements.txt

# Run locally
flask --app api/index run
```

API will be available at `http://localhost:5000/api/ai`

---

## Project Structure

```
LlamaCoder/
├── api/
│   └── index.py       # Flask app + Together AI integration
├── requirements.txt   # Python dependencies (flask, httpx)
├── vercel.json        # Vercel deployment config
└── README.md
```

---

## Tech Stack

- **Runtime** — Python 3.x
- **Framework** — Flask
- **HTTP Client** — httpx (async)
- **AI Backend** — Together AI / LlamaCode
- **Deployment** — Vercel (Serverless)

---

## Credits

Made by **MK Hossain**
- Telegram: [@bizft](https://t.me/bizft)
- Handle: `@mk_hossain`
