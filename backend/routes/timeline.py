from fastapi import APIRouter, HTTPException
from models import TimelineUpdateRequest, TimelineEvent
from prompts.timeline import timeline_prompt
from gemini_client import call_gemini
from utils import safe_gemini_json_call
from typing import List

router = APIRouter(prefix="/timeline", tags=["Timeline"])


@router.post("/update", response_model=List[TimelineEvent])
def update_timeline(request: TimelineUpdateRequest):
    """
    Updates the investigation timeline using new events.
    """
    try:
        prompt = timeline_prompt(
            request.existing_timeline,
            request.new_events
        )

        updated_timeline = safe_gemini_json_call(call_gemini, prompt)

        if not isinstance(updated_timeline, list):
            raise ValueError("Timeline output is not a list")

        return updated_timeline

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Timeline update failed: {str(e)}"
        )
