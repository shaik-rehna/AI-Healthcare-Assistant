def build_prompt(symptoms):

    return f"""
You are a medical triage assistant.

Symptoms:
{symptoms}

Return ONLY:

Possible concerns:
- 3 bullet points

Urgency:
One word only

Recommended next steps:
- 3 bullet points

Do not add explanations.
"""