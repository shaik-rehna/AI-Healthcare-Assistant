from gen_ai_healthcare_report_gen.app.prompts.triage_prompt import build_prompt

from gen_ai_healthcare_report_gen.app.models.inference_finetuned import (
generate_finetuned_response
)

from gen_ai_healthcare_report_gen.app.outputs.parser import parse_output

from gen_ai_healthcare_report_gen.app.outputs.report_generator import (
generate_pdf
)


symptoms = input(
"Enter symptoms: "
)

prompt = build_prompt(
symptoms
)

raw_output = generate_finetuned_response(
prompt
)

print(raw_output)


parsed = parse_output(
raw_output
)

generate_pdf(
parsed
)

print(
"Fine-tuned medical report saved."
)