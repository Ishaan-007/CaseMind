import json
import re
from typing import Any


def extract_json_from_text(text: str) -> Any:
    """
    Gemini sometimes wraps JSON in markdown or text.
    This safely extracts the first valid JSON block.
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try extracting JSON inside code blocks
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    raise ValueError("Unable to extract valid JSON from Gemini response")


import json
import re

def safe_gemini_json_call(call_fn, prompt: str):
    raw = call_fn(prompt)

    # Try direct JSON
    try:
        return json.loads(raw)
    except:
        pass

    # Try extracting JSON block
    match = re.search(r'(\[.*\]|\{.*\})', raw, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except:
            pass

    raise ValueError("Unable to extract valid JSON from Gemini response")



def normalize_text(text: str) -> str:
    """
    Basic cleanup for FIRs, transcripts, OCR output.
    """
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def confidence_from_keywords(text: str) -> str:
    """
    Very lightweight heuristic for demo purposes.
    """
    text = text.lower()
    if any(word in text for word in ["clearly", "confirmed", "definitely"]):
        return "high"
    if any(word in text for word in ["possibly", "appears", "likely"]):
        return "medium"
    return "low"


def build_standard_response(message: str, data: Any = None) -> dict:
    """
    Ensures consistent API responses.
    """
    return {
        "status": "success",
        "message": message,
        "data": data
    }
