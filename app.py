import streamlit as st

from src.prompts.triage_prompt import build_prompt

from src.models.inference_finetuned import (
generate_finetuned_response
)

from src.outputs.parser import parse_output

from src.outputs.report_generator import generate_pdf


st.set_page_config(
    page_title="AI Healthcare Assistant",
    layout="centered"
)

st.title(
"AI Healthcare Assistant"
)

st.write(
"Please enter the symptoms your currently facing..."
)


symptoms = st.text_area(
    "Symptoms",
    placeholder=
    "Example: fever, cough, fatigue"
)


if st.button(
"Generate Healthcare Report"
):

    with st.spinner(
    "Generating report..."
    ):

        prompt = build_prompt(
            symptoms
        )

        raw_output = (
          generate_finetuned_response(
             prompt
          )
        )


        # st.subheader("Raw Model Output")
        # st.text(raw_output)

        parsed = parse_output(
            raw_output
        )

        generate_pdf(
            parsed
        )


    st.success(
    "Report generated."
    )


    st.subheader(
    "Possible Concerns"
    )

    for c in parsed[
    "possible_concerns"
    ]:
        st.write(
        f"- {c}"
        )


    # st.subheader(
    # "Urgency"
    # )

    # urgency = parsed[
    # "urgency"
    # ]


    # if "High" in urgency \
    # or "Emergency" in urgency:

    #     st.error(
    #     urgency
    #     )

    # elif "Moderate" in urgency:

    #     st.warning(
    #     urgency
    #     )

    # else:

    #     st.success(
    #     urgency
    #     )


    st.subheader(
    "Recommended Next Steps"
    )

    for step in parsed[
    "recommended_next_steps"
    ]:

        st.write(
        f"- {step}"
        )


    with open(
    "health_report.pdf",
    "rb"
    ) as f:

        st.download_button(
            label=
            "Download PDF Report",

            data=f,

            file_name=
            "health_report.pdf",

            mime=
            "application/pdf"
        )