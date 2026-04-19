import re


def clean_bullets(section):

    lines = section.split("\n")

    items = []

    for line in lines:

        line = line.strip()

        if line.startswith("-"):
            items.append(
                line.replace("-", "").strip()
            )

    return items


def parse_output(text):

    concerns_match = re.findall(
        r"Possible concerns:?(.*?)Urgency:?",
        text,
        re.DOTALL
    )

    urgency_match = re.findall(
        r"Urgency:?(.*?)Recommended next steps:?",
        text,
        re.DOTALL
    )

    steps_match = re.findall(
        r"Recommended next steps:?(.*)",
        text,
        re.DOTALL
    )


    if not concerns_match:

        return {

            "possible_concerns":
                ["Parsing failed"],

            "urgency":
                "Unknown",

            "recommended_next_steps":
                [
                 "Model output format unexpected"
                ]
        }


    concerns_raw = concerns_match[0]


    urgency_raw = (
        urgency_match[0].strip()
        if urgency_match
        else "Unknown"
    )


    steps_raw = (
        steps_match[0]
        if steps_match
        else ""
    )


    return {

        "possible_concerns":
            clean_bullets(
                concerns_raw
            ),

        "urgency":
            urgency_raw,

        "recommended_next_steps":
            clean_bullets(
                steps_raw
            )
    }