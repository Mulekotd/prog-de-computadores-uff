from typing import Any, Callable
import time


def calculate_execution_time(callback_fn: Callable) -> tuple[float, Any]:
    start_time: float = time.time()
    result: Any = callback_fn()
    end_time: float = time.time()
    return (end_time - start_time) * 1000, result or None

def get_breakline(type: str) -> str:
    breaklines: dict[str, str] = {
        "TWO_LINES": "\n\n",
        "NEW_LINE": "\n",
        "NO_BREAK": ""
    }

    return breaklines[type]
