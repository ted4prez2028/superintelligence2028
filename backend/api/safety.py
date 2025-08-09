import os, time, json
from fastapi import HTTPException, Request
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
LOG = os.path.join(os.path.dirname(__file__), "..", "audit.log")

async def check_text(text: str) -> None:
    r = client.moderations.create(model="omni-moderation-latest", input=text)
    if r.results[0].flagged:
        raise HTTPException(status_code=400, detail="Unsafe content")

def audit(request: Request, action: str) -> None:
    user = getattr(request.client, "host", "unknown")
    with open(LOG, "a") as f:
        f.write(json.dumps({"ts": time.time(), "user": user, "action": action}) + "\n")
