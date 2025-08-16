import json, time
from typing import Any
from . import memory

async def record_result(task_id: str, score: float, notes: str) -> None:
    """Store evaluation feedback for later analysis."""
    text = json.dumps({"score": score, "notes": notes, "ts": time.time()})
    memory.upsert(f"metric:{task_id}", text)

async def refine_prompts(_payload: Any = None) -> dict:
    """Heuristic prompt refinement using stored evaluation feedback."""
    data = memory.query("evaluation feedback", top_k=20).get("results", [])
    # Placeholder heuristic: count recent feedback entries
    return {"refined": len(data)}
