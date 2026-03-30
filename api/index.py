from flask import Flask, request, jsonify
import httpx
import asyncio
import json

app = Flask(__name__)

BASE_URL = "https://llamacoder.together.ai"

MODEL_MAP = {
    "fast": "zai-org/GLM-4.6",
    "pro": "Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
    "thinking": "deepseek-ai/DeepSeek-V3.1"
}

def resolve_model(name):
    return MODEL_MAP.get(name, name)

async def create_chat(client, prompt, model, image):
    payload = {
        "prompt": prompt,
        "model": model,
        "quality": "low"
    }

    if image:
        payload["screenshotUrl"] = image

    res = await client.post(
        f"{BASE_URL}/api/create-chat",
        json=payload,
        headers={
            "content-type": "application/json",
            "accept": "*/*",
            "origin": BASE_URL,
            "referer": BASE_URL + "/",
            "user-agent": "Mozilla/5.0",
            "x-requested-with": "mark.via.gp"
        }
    )

    return res.json().get("lastMessageId")

async def stream_response(client, message_id, model):
    res = await client.post(
        f"{BASE_URL}/api/get-next-completion-stream-promise",
        content=json.dumps({
            "messageId": message_id,
            "model": model
        }),
        headers={
            "content-type": "text/plain;charset=UTF-8",
            "accept": "*/*",
            "origin": BASE_URL,
            "referer": BASE_URL + "/",
            "user-agent": "Mozilla/5.0",
            "x-requested-with": "mark.via.gp"
        }
    )

    output = ""
    for line in res.text.splitlines():
        try:
            obj = json.loads(line)
            delta = obj["choices"][0]["delta"]
            if delta.get("content"):
                output += delta["content"]
        except:
            continue

    return output.strip()

async def generate(prompt, model, image):
    model = resolve_model(model)

    async with httpx.AsyncClient(timeout=60) as client:
        message_id = await create_chat(client, prompt, model, image)
        if not message_id:
            return "Error: message_id not found"
        return await stream_response(client, message_id, model)

@app.route("/api/ai")
def ai():
    prompt = request.args.get("prompt")
    model = request.args.get("model", "fast")
    image = request.args.get("image")

    if not prompt:
        return jsonify({"status": False, "error": "prompt required"})

    result = asyncio.run(generate(prompt, model, image))

    return jsonify({
        "status": True,
        "model": model,
        "response": result
    })

def handler(request):
    return app(request.environ, lambda *args: None)
