import time, platform
import psutil

_state = {}

def snapshot():
    """Capture system resource snapshot."""
    _state.update({
        "ts": time.time(),
        "cpu": psutil.cpu_percent(),
        "mem": psutil.virtual_memory()._asdict(),
        "platform": platform.platform(),
    })
    return _state
