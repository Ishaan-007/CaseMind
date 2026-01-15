from fastapi import APIRouter
from models import GraphResponse
from gemini_client import call_gemini
from prompts.graph import graph_prompt
from utils import safe_gemini_json_call

router = APIRouter(prefix="/graph", tags=["Entity Graph"])


@router.post("/build", response_model=GraphResponse)
def build_entity_graph(case_data: dict):
    """
    Builds a connected graph of all entities in the case.
    """
    prompt = graph_prompt(case_data)
    graph_json = safe_gemini_json_call(call_gemini, prompt)
    return graph_json
