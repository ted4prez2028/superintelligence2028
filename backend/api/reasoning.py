from typing import Dict, Any
from .runners import client

async def run_reasoning(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Run advanced chain-of-thought reasoning using the Responses API."""
    question = payload.get("question", "")
    r = client.responses.create(
        model="gpt-4.1-mini",
        reasoning={"effort": "medium"},
        input=[{"role": "user", "content": f"Reason step-by-step and answer:\n{question}"}]
    )
    return {
        "thoughts": getattr(r, "output_text", ""),
        "final": getattr(r, "output_text", "")
    }
