from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

from peft import PeftModel


base_model = "google/gemma-2-2b-it"

adapter_path = "gemma-medical-lora"


tokenizer = AutoTokenizer.from_pretrained(
    base_model
)

model = AutoModelForCausalLM.from_pretrained(
    base_model
)

model = PeftModel.from_pretrained(
    model,
    adapter_path
)


def generate_finetuned_response(prompt):

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )


    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        max_length=None,
        do_sample=False
    )


    decoded = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )


    # Remove prompt echo
    response = decoded.replace(
        prompt,
        ""
    )


    # Remove junk artifacts
    junk_tokens = [
        "- ...",
        "\\end{document}",
        "</s>",
        "<eos>"
    ]

    for token in junk_tokens:

        response = response.replace(
            token,
            ""
        )


    # Keep only structured section
    if "Possible concerns:" in response:

        response = response[
            response.index(
                "Possible concerns:"
            ):
        ]

    else:

        return """
Possible concerns:
- Unable to parse model output

Urgency:
Unknown

Recommended next steps:
- Please regenerate report
"""


    return response.strip()