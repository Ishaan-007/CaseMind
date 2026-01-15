def evidence_prompt(
    fir_context: dict,
    evidence_type: str,
    evidence_summary: str,
    timestamp: str | None = None,
    source: str | None = None
) -> str:
    return f"""
You are an AI police investigation assistant.

FIR CONTEXT:
{fir_context}

EVIDENCE TYPE:
{evidence_type}

EVIDENCE SUMMARY:
{evidence_summary}

METADATA:
- Timestamp: {timestamp}
- Source: {source}

TASK:
1. Extract key findings from the evidence.
2. Identify any victims, suspects, witnesses, locations, or objects.
3. Infer possible timeline events.
4. Assess confidence level (low/medium/high).
5. Highlight anything that supports or contradicts the FIR.

OUTPUT FORMAT (STRICT JSON ONLY):
{{
  "key_findings": [],
  "extracted_entities": {{
    "victims": [],
    "suspects": [],
    "witnesses": [],
    "locations": [],
    "objects": []
  }},
  "inferred_timeline_events": [],
  "confidence_level": ""
}}

Do NOT include explanations outside JSON.
"""
