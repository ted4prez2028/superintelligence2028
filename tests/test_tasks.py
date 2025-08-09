import asyncio
import pytest
from backend.api import tasks


@pytest.mark.asyncio
async def test_task_processing_marks_done_and_clears_queue():
    async def dummy(payload):
        await asyncio.sleep(0)
        return payload.get("value", 1)

    await tasks.start_workers(1)
    tid = tasks.submit(dummy, {"value": 42})
    await asyncio.wait_for(tasks._q.join(), timeout=1)

    assert tasks.status(tid)["status"] == "done"
