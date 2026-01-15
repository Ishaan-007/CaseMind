from fastapi import APIRouter
from pydantic import BaseModel
from gemini_client import call_gemini
from prompts.evidence import evidence_prompt
import json

router = APIRouter()

class EvidenceInput(BaseModel):
    fir_context: dict
    evidence_description: str

@router.post("/process-evidence")
def process_evidence(data: EvidenceInput):
    prompt = evidence_prompt(data.fir_context, data.evidence_description)
    response = call_gemini(prompt)
    return json.loads(response)
